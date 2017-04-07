import unittest

from domain.encounter import EncounterBuilder
from domain.state.daystate import DayState
from domain.day import *
from event.action import DialogOver, FloorSelected


class DayStateTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ignore_encounter_path(self):
        A_DAY = 1
        A_STAGE_SRC = 4
        A_STAGE_DEST = 2
        encounter = EncounterBuilder().with_stage_src(A_STAGE_SRC)\
                                    .with_stage_dest(A_STAGE_DEST).build()
        self.A_DAY_STATE = DayState(Day(A_DAY, load_from_json=False, encounters=[encounter]))

        self.assertEqual(self.A_DAY_STATE.introduce_next_client, self.A_DAY_STATE.next_substate)
        self.A_DAY_STATE.exec()

        self.assertEqual(self.A_DAY_STATE.anime.wait_for_end_animation, self.A_DAY_STATE.next_substate)
        self.A_DAY_STATE.exec()
        self.assertEqual(self.A_DAY_STATE.anime.wait_for_end_animation, self.A_DAY_STATE.next_substate)
        self.A_DAY_STATE.exec(None, [DialogOver()])
        self.assertEqual(self.A_DAY_STATE.finish_highlight_stage_number, self.A_DAY_STATE.next_substate)

        # Wait for player to select level
        self.A_DAY_STATE.exec()
        self.assertEqual(self.A_DAY_STATE.wait_for_player_input, self.A_DAY_STATE.next_substate)
        self.A_DAY_STATE.exec()
        self.assertEqual(self.A_DAY_STATE.wait_for_player_input, self.A_DAY_STATE.next_substate)

        # Move elevator
        A_FLOOR = 1
        self.A_DAY_STATE.exec(None, [FloorSelected(A_FLOOR)])
        self.assertEqual(self.A_DAY_STATE.anime.wait_for_end_animation, self.A_DAY_STATE.next_substate)
        self.A_DAY_STATE.exec(None, [DialogOver()])
        self.assertEqual(self.A_DAY_STATE.ignore_client, self.A_DAY_STATE.next_substate)

        # Get yield by boss and loose money
        self.A_DAY_STATE.exec()
        self.assertEqual(self.A_DAY_STATE.dialog.wait_for_end_dialog, self.A_DAY_STATE.next_substate)
        self.A_DAY_STATE.exec()
        self.assertEqual(self.A_DAY_STATE.dialog.wait_for_end_dialog, self.A_DAY_STATE.next_substate)
        self.A_DAY_STATE.exec(None, [DialogOver()])

        # Next client
        self.assertEqual(self.A_DAY_STATE.introduce_next_client, self.A_DAY_STATE.next_substate)





