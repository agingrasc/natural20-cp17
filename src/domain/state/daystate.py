from domain.blackbox import Blackbox
from domain.state.state import State
from display.action.dialog import Dialog
from domain.state.substate import DialogSubState, AnimationSubState
from event.action import UserKeyAction, FloorSelected


class DayState(State):
    def __init__(self, day):
        super().__init__(self.introduce_next_client)
        self.day = day
        self.finish = False
        Blackbox.stage = self.day.start_stage

    def introduce_next_client(self, dt, actions):
        self.current_encounter = self.day.pop_triggable_encounter(Blackbox().flags)

        if self.current_encounter is None:
            self.next_substate = self.end_day
        else:
            print(">>> Level: {} Blinking".format(self.current_encounter.raw_json['stage_src']))
            self.anime = AnimationSubState("elevator_light", self, self.finish_highlight_stage_number)

    def finish_highlight_stage_number(self, dt, actions):
        if Blackbox().stage == self.current_encounter.stage_src:
            self.change_substate(self.open_door)
        else:
            self.change_substate(self.wait_for_player_input)

    def wait_for_player_input(self, dt, actions):
        for action in actions:
            if isinstance(action, FloorSelected):
                # TODO have an action if the dest is wrong
                if action.data['floor'] == Blackbox.stage:
                    self.change_substate(self.open_door)
                elif action.data['floor'] == self.current_encounter.stage_src:
                    self.anime = AnimationSubState("move the elevator to client", self, self.open_door)
                else:
                    self.anime = AnimationSubState("move the elevator to knownwhere", self, self.ignore_client)

    # TODO find a juicer way of doing that:
    def open_door(self, dt, actions):
        self.anime = AnimationSubState("opening door", self, self.encounter_enter_elevator)
    def encounter_enter_elevator(self, dt, actions):
        self.anime = AnimationSubState("client walking in elevator", self, self.greet_encounter)
    def greet_encounter(self, dt, actions):
        self.dialog = DialogSubState(self.current_encounter.name, self.current_encounter.say_greeting(), self, self.close_door)
    def close_door(self, dt, actions):
        self.anime = AnimationSubState("close door", self, self.dialog_with_encounter)
    def dialog_with_encounter(self, dt, actions):
        self.dialog = DialogSubState(self.current_encounter.name, self.current_encounter.dialogs, self, self.wait_for_player_input_with_encounter)

    def wait_for_player_input_with_encounter(self, dt, actions):
        for action in actions:
            if isinstance(action, FloorSelected):
                # TODO have an action if the dest is wrong
                Blackbox().stage = action.data['floor']
                if action.data['floor'] == self.current_encounter.stage_dest:
                    self.anime = AnimationSubState("move client to dest", self, self.reach_dest)
                else:
                    self.anime = AnimationSubState("move client to knownwhere", self, self.ignore_dest)

    # Endings
    def reach_dest(self, dt, actions):
        Blackbox().flags += self.current_encounter.happy_ending_flag
        Blackbox().tips += self.current_encounter.tips
        self.dialog = DialogSubState(self.current_encounter.name, self.current_encounter.say_farewell(), self, self.introduce_next_client)

    def ignore_dest(self, dt, actions):
        Blackbox().flags += self.current_encounter.ignore_dest_flag
        self.dialog = DialogSubState(self.current_encounter.name, self.current_encounter.say_insult(), self, self.introduce_next_client)

    def ignore_client(self, dt, actions):
        Blackbox().stage = self.current_encounter.stage_src
        Blackbox().flags += self.current_encounter.ignore_client_flag
        # TODO add remove pourboire
        self.dialog = DialogSubState("BOSS", "Le boss chiale todo \ncreer un dict pour sa", self, self.introduce_next_client)

    def end_day(self, dt, actions):
        self.finish = True

    def is_finish(self):
        return self.finish
