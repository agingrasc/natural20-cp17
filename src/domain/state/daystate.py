from domain.state.state import State
from display.action.dialog import Dialog
from event.action import DialogOver


class DialogSubState:
    """
    Handle a sequence of substate to output a dialog and return to substate when finished
    """
    def __init__(self, text: str, parentState, returnSubstateCallback):
        self.parentState = parentState
        self.returnSubstateCallback = returnSubstateCallback

        self.current_dialog = Dialog(text)
        self.parentState.next_substate = self.wait_for_end_dialog


    def wait_for_end_dialog(self, dt, actions):
        for action in actions:
            if isinstance(action, DialogOver):
                self.return_to_parent_state()
        else:
            return self.current_dialog

    def return_to_parent_state(self):
        self.parentState.next_substate = self.returnSubstateCallback

class DayState(State):
    def __init__(self, day):
        super().__init__(self.introduce_next_client)
        self.day = day

    def introduce_next_client(self, dt, actions):
        self.current_encounter = self.day.pop_triggable_encounter([])
        if self.current_encounter is None:
            self.next_substate = self.end_day
        else
            return self.change_substate_and_exec(self.move_client_to_elevator)

    def move_client_to_elevator(self, dt, actions):
        # Should wait for end of animate
        self.dialog = DialogSubState(self.current_encounter.say_greeting(), self, self.init_player_input)

    def init_player_input(self, dt, actions):
        pass

    def end_day(self, dt, actions):
        pass


    def is_finish(self):
        False