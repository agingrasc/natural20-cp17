from display.action.dialog import Dialog
from event.action import UserKeyAction

# TODO create interface

class AnimationSubState:
    """
    Handle a sequence of substate to output a dialog and return to substate when finished
    """
    def __init__(self, animation_id, parentState, returnSubstateCallback):
        self.parentState = parentState
        self.returnSubstateCallback = returnSubstateCallback

        self.current_dialog = Dialog(animation_id)# TODO should use a animation action
        self.parentState.change_substate(self.wait_for_end_animation)


    def wait_for_end_animation(self, dt, actions):
        for action in actions:
            if isinstance(action, UserKeyAction):
                self.return_to_parent_state()
        else:
            return self.current_dialog

    def return_to_parent_state(self):
        self.parentState.next_substate =  self.returnSubstateCallback


class DialogSubState:
    """
    Handle a sequence of substate to output a dialog and return to substate when finished
    """
    def __init__(self, text: str, parentState, returnSubstateCallback):
        self.parentState = parentState
        self.returnSubstateCallback = returnSubstateCallback

        self.current_dialog = Dialog(text)
        self.parentState.change_substate(self.wait_for_end_dialog)

    def wait_for_end_dialog(self, dt, actions):
        for action in actions:
            if isinstance(action, UserKeyAction):
                self.return_to_parent_state()
        else:
            return self.current_dialog

    def return_to_parent_state(self):
        self.parentState.next_substate =  self.returnSubstateCallback
