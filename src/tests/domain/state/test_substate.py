import unittest

from display.action.dialog import Dialog
from domain.day import Day
from domain.state.daystate import DayState
from domain.state.substate import DialogSubState
from event.action import DialogOver


def RETURN_CALLBACK():
    pass

class DialogSubStateTest(unittest.TestCase):
    def setUp(self):
        A_DAY = 1
        self.A_TEXT = "hello, world"
        self.A_PARENT_STATE = DayState(Day(A_DAY, load_from_json=False, encounters=[]))

    def tearDown(self):
        pass


    def test_given_a_text_and_a_parent_state_when_parent_executed_then_a_dialog_with_that_text_is_return(self):
        dialogSubState = DialogSubState(self.A_TEXT, self.A_PARENT_STATE, RETURN_CALLBACK)

        dialogAction = self.A_PARENT_STATE.exec()

        self.assertIsInstance(dialogAction, Dialog)
        self.assertEqual(self.A_TEXT, dialogAction.text)

    def test_given_dialog_over_action_when_parent_executed_then_parent_next_state_is_return_callback(self):
        dialogSubState = DialogSubState(self.A_TEXT, self.A_PARENT_STATE, RETURN_CALLBACK)

        self.A_PARENT_STATE.exec(None, [DialogOver()])

        self.assertEqual(RETURN_CALLBACK, self.A_PARENT_STATE.next_substate)