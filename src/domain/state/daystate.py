from domain.state.state import State
from display.action.dialog import Dialog
from domain.state.substate import DialogSubState, AnimationSubState
from event.action import DialogOver, FloorSelected


class DayState(State):
    def __init__(self, day):
        super().__init__(self.introduce_next_client)
        self.day = day
        self.finish = False
        self.stage_number = self.day.start_stage
        self.flag = []


    def introduce_next_client(self, dt, actions):
        self.current_encounter = self.day.pop_triggable_encounter([])
        if self.current_encounter is None:
            self.next_substate = self.end_day
        else:
            self.anime = AnimationSubState("elevator_light", self, self.finish_highlight_stage_number)


    def finish_highlight_stage_number(self, dt, actions):
        if self.stage_number == self.current_encounter.stage_src:
            self.change_substate(self.open_door)
        else:
            self.change_substate(self.wait_for_player_input)


    def wait_for_player_input(self, dt, actions):
        for action in actions:
            if isinstance(action, FloorSelected):
                self.anime = AnimationSubState("move the elevator", self, self.ignore_client)
                # TODO have an action if the dest is wrong
                #if action.data == 0 :
                #    ...

    def ignore_client(self, dt, actions):
        self.flag += self.current_encounter.ignore_client_flag
        # TODO add remove cash
        self.dialog = DialogSubState("Le boss chiale todo creer un dict pour sa", self, self.introduce_next_client)


    def open_door(self, dt, actions):
        pass


    def move_client_to_elevator(self, dt, actions):
        # Should wait for end of animate
        self.dialog = DialogSubState(self.current_encounter.say_greeting(), self, self.init_player_input)

    def init_player_input(self, dt, actions):
        pass

    def end_day(self, dt, actions):
        self.finish = True

    def is_finish(self):
        return self.finish
