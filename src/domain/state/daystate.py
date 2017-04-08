from display.action.animation import SpriteAnimationAction, ButtonAnimationAction
from display.action.button import ButtonPushedAction, ButtonReleasedAction
from display.action.client import ClientAction, NoClientAction
from display.action.elavatorgate import ElevatorGateOpenAction, ElevatorGateCloseAction
from display.action.floorindicator import FloorIndicatorAction
from display.action.floorcall import FloorCallAction
from display.action.inoutclient import InOutClientAction, ClientInAction, ClientOutAction
from domain.blackboard import Blackboard
from domain.state.state import State
from display.action.dialog import Dialog
from domain.state.substate import DialogSubState, AnimationSubState
from event.action import UserKeyAction, FloorSelected


class DayState(State):
    def __init__(self, day):
        super().__init__(self.introduce_next_client)
        self.day = day
        self.finish = False
        self.warning = 0
        Blackboard().stage = self.day.start_stage

    def introduce_next_client(self, dt, actions):
        self.current_encounter = self.day.pop_triggable_encounter(Blackboard().flags)

        if self.current_encounter is None:
            self.next_substate = self.end_day
        else:
            print(">>> Level: {} Blinking".format(self.current_encounter.raw_json['stage_src']))
            self.change_substate(self.finish_highlight_stage_number)

    def finish_highlight_stage_number(self, dt, actions):
        if Blackboard().stage == self.current_encounter.stage_src:
            self.change_substate(self.open_door)
        else:
            self.warning = 0
            self.change_substate(self.wait_for_player_input)
            return FloorCallAction(self.current_encounter.stage_src)

    def wait_for_player_input(self, dt, actions):
        for action in actions:
            if isinstance(action, FloorSelected):
                animation = FloorIndicatorAction(Blackboard().stage, action.data['floor'])
                if action.data['floor'] == self.current_encounter.stage_src:
                    self.anime = AnimationSubState(animation, self, self.open_door)
                elif action.data['floor'] == Blackboard().stage:
                    self.change_substate(self.ignore_client)
                else:
                    self.anime = AnimationSubState(animation, self, self.ignore_client)
                Blackboard().stage = action.data['floor']
                return ButtonPushedAction(action.data['floor'])

    # TODO find a juicer way of doing that:
    def open_door(self, dt, actions):
        #self.anime = AnimationSubState(Dialog("ANIMATION", "opening door"), self, self.encounter_enter_elevator)
        self.anime = AnimationSubState(ElevatorGateOpenAction(), self, self.encounter_enter_elevator)

        return [ButtonReleasedAction(Blackboard().stage), FloorCallAction(None)]
    def encounter_enter_elevator(self, dt, actions):
        self.anime = AnimationSubState(ClientInAction(self.current_encounter.name), self, self.greet_encounter)
    def greet_encounter(self, dt, actions):
        self.dialog = DialogSubState(self.current_encounter.name, self.current_encounter.say_greeting(), self, self.close_door)
        return ClientAction(self.current_encounter.name)
    def close_door(self, dt, actions):
        #self.anime = AnimationSubState(Dialog("ANIMATION", "close door"), self, self.dialog_with_encounter)
        self.anime = AnimationSubState(ElevatorGateCloseAction(), self, self.dialog_with_encounter)
    def dialog_with_encounter(self, dt, actions):
        self.dialog = DialogSubState(self.current_encounter.name, self.current_encounter.dialogs, self, self.wait_for_player_input_with_encounter)

    def wait_for_player_input_with_encounter(self, dt, actions):
        for action in actions:
            if isinstance(action, FloorSelected):
                animation = FloorIndicatorAction(Blackboard().stage, action.data['floor'])
                Blackboard().stage = action.data['floor']
                if action.data['floor'] == self.current_encounter.stage_dest:
                    self.anime = AnimationSubState(animation, self, self.reach_dest)
                else:
                    self.anime = AnimationSubState(animation, self, self.ignore_dest)
                return ButtonPushedAction(action.data['floor'])

    def open_door_encounter_leave(self, dt, actions):
        self.anime = AnimationSubState(ElevatorGateOpenAction(), self, self.encounter_leave)
    def encounter_leave(self, dt, actions):
        self.anime = AnimationSubState(ClientOutAction(self.current_encounter.name), self, self.close_door_encounter_leave)
        return NoClientAction()
    def close_door_encounter_leave(self, dt, actions):
        #self.anime = AnimationSubState(Dialog("ANIMATION", "close door"), self, self.introduce_next_client)
        self.anime = AnimationSubState(ElevatorGateCloseAction(), self, self.introduce_next_client)

    # Endings
    def reach_dest(self, dt, actions):
        Blackboard().flags += self.current_encounter.happy_ending_flag
        Blackboard().tips += self.current_encounter.tips
        self.dialog = DialogSubState(self.current_encounter.name, self.current_encounter.say_farewell(), self, self.open_door_encounter_leave)
        return ButtonReleasedAction(Blackboard().stage)

    def ignore_dest(self, dt, actions):
        Blackboard().flags += self.current_encounter.ignore_dest_flag
        self.dialog = DialogSubState(self.current_encounter.name, self.current_encounter.say_insult(), self, self.open_door_encounter_leave)
        return ButtonReleasedAction(Blackboard().stage)

    def ignore_client(self, dt, actions):
        if self.warning < 1:
            if self.current_encounter.has_boss_complain():
                self.dialog = DialogSubState("[INTERCOM] Boss Daniel", self.current_encounter.say_boss_complain(),
                                             self, self.wait_for_player_input)
            self.warning += 1
        else:
            Blackboard().flags += self.current_encounter.ignore_client_flag
            Blackboard().tips -= self.current_encounter.penality
            self.change_substate(self.introduce_next_client)
        return ButtonReleasedAction(Blackboard().stage)

    def end_day(self, dt, actions):
        self.finish = True

    def is_finish(self):
        return self.finish
