from display.action.dialog import Dialog
from display.action.interface import IDomainAction
from event.action import UserKeyAction

# TODO create interface

class AnimationSubState:
    """
    Handle a sequence of substate to output a dialog and return to substate when finished
    """
    def __init__(self, animation: IDomainAction, parentState, returnSubstateCallback):
        self.parentState = parentState
        self.returnSubstateCallback = returnSubstateCallback

        self.current_animation = animation
        self.parentState.change_substate(self.wait_for_end_animation)


    def wait_for_end_animation(self, dt, actions):
        if self.current_animation.finished:
            self.return_to_parent_state()
        else:
            return self.current_animation
        # for action in actions:
        #     # TODO add finish to animation
        #     if isinstance(action, UserKeyAction):
        #         self.return_to_parent_state()
        # else:

    def return_to_parent_state(self):
        self.parentState.next_substate =  self.returnSubstateCallback


class DialogSubState:
    """
    Handle a sequence of substate to output a dialog and return to substate when finished
    """
    def __init__(self, name: str, text: str, parentState, returnSubstateCallback):
        self.parentState = parentState
        self.returnSubstateCallback = returnSubstateCallback

        self.current_dialog = Dialog(name, text)
        self.parentState.change_substate(self.wait_for_end_dialog)

    def wait_for_end_dialog(self, dt, actions):
        for action in actions:
            if isinstance(action, UserKeyAction):
                if self.current_dialog.finished:
                    self.return_to_parent_state()
                    break
                else:
                    self.current_dialog.finished = True
                    break
        return self.current_dialog

    def return_to_parent_state(self):
        self.parentState.next_substate =  self.returnSubstateCallback
