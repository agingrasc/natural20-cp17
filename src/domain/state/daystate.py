from domain.state.state import State
from display.action.dialog import Dialog
from event.action import DialogOver


class DayState(State):
    def __init__(self, day):
        super().__init__(self.introduce_next_client)
        self.day = day

    def introduce_next_client(self, dt, actions):
        self.current_client = self.day.pop_clients()
        return self.change_substate_and_exec(self.move_client_to_elevator)

    def move_client_to_elevator(self, dt, actions):
        # Should wait for end of animate
        self.next_substate = self.init_dialog

    def init_dialog(self, dt, actions):
        self.current_dialog = Dialog(self.current_client.greet())
        self.next_substate = self.wait_for_end_dialog
        return self.current_dialog

    def wait_for_end_dialog(self, dt, actions):
        for action in actions:
            if isinstance(action, DialogOver):
                self.next_substate = self.init_player_input
        else:
            return self.current_dialog

    def init_player_input(self, dt, actions):
        pass


    def is_finish(self):
        False