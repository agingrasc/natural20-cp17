import unittest

from display.button import NUMBER_OF_BUTTONS_COLS, NUMBER_OF_BUTTONS_ROWS, ButtonBuilder
from domain.encounter import EncounterBuilder
from domain.state.daystate import DayState
from domain.day import *
from event.action import FloorSelected, UserKeyAction
from display import button


class DayStateTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def create_button(self):
        for i in range(NUMBER_OF_BUTTONS_COLS):
            for j in range(NUMBER_OF_BUTTONS_ROWS):
                floor = button.compute_floor(i, j)
                ButtonBuilder().add_button_hack_for_ut( i, j)

    def wait_for_animation_assert_state(self, expected_state):
        self.A_DAY_STATE.exec()
        self.assertEqual(self.A_DAY_STATE.anime.wait_for_end_animation, self.A_DAY_STATE.next_substate)
        self.A_DAY_STATE.anime.current_animation.finished = True
        self.A_DAY_STATE.exec()
        self.assertEqual(expected_state, self.A_DAY_STATE.next_substate)

    def wait_for_dialog_assert_state(self, expected_state):
        self.A_DAY_STATE.exec()
        self.assertEqual(self.A_DAY_STATE.dialog.wait_for_end_dialog, self.A_DAY_STATE.next_substate)
        self.A_DAY_STATE.exec(None, [UserKeyAction()])
        self.A_DAY_STATE.exec(None, [UserKeyAction()])
        self.assertEqual(expected_state, self.A_DAY_STATE.next_substate)

    def test_ignore_encounter_path(self):
        self.create_button()
        A_DAY = 1
        A_STAGE_SRC = 4
        A_STAGE_DEST = 2
        encounter = EncounterBuilder().with_stage_src(A_STAGE_SRC)\
                                      .with_stage_dest(A_STAGE_DEST)\
                                      .with_boss_complains([""]).build()
        self.A_DAY_STATE = DayState(Day(A_DAY, load_from_json=False, encounters=[encounter], starting_stage=1))

        self.assertEqual(self.A_DAY_STATE.introduce_next_client, self.A_DAY_STATE.next_substate)
        self.A_DAY_STATE.exec()

        self.assertEqual(self.A_DAY_STATE.anime.wait_for_end_animation, self.A_DAY_STATE.next_substate)
        self.wait_for_animation_assert_state(self.A_DAY_STATE.finish_highlight_stage_number)

        # Wait for player to select level
        self.A_DAY_STATE.exec()
        self.assertEqual(self.A_DAY_STATE.wait_for_player_input, self.A_DAY_STATE.next_substate)
        self.A_DAY_STATE.exec()
        self.assertEqual(self.A_DAY_STATE.wait_for_player_input, self.A_DAY_STATE.next_substate)

        # Move elevator
        self.A_DAY_STATE.exec(None, [FloorSelected(A_STAGE_DEST)])
        #self.assertEqual(self.A_DAY_STATE.anime.wait_for_end_animation, self.A_DAY_STATE.next_substate)
        #self.A_DAY_STATE.exec(None, [UserKeyAction()])
        #self.assertEqual(self.A_DAY_STATE.ignore_client, self.A_DAY_STATE.next_substate)
        self.wait_for_animation_assert_state(self.A_DAY_STATE.ignore_client)

        # Get yield by boss and loose money
        self.A_DAY_STATE.exec()
        self.assertEqual(self.A_DAY_STATE.dialog.wait_for_end_dialog, self.A_DAY_STATE.next_substate)
        self.wait_for_dialog_assert_state(self.A_DAY_STATE.introduce_next_client)

    def test_happy_path(self):
        self.create_button()
        A_DAY = 1
        A_STAGE_SRC = 4
        A_STAGE_DEST = 2
        encounter = EncounterBuilder().with_stage_src(A_STAGE_SRC)\
                                    .with_stage_dest(A_STAGE_DEST).build()
        self.A_DAY_STATE = DayState(Day(A_DAY, load_from_json=False, encounters=[encounter]))

        self.wait_for_animation_assert_state(self.A_DAY_STATE.finish_highlight_stage_number)

        # Wait for player to select level
        self.A_DAY_STATE.exec()
        self.assertEqual(self.A_DAY_STATE.wait_for_player_input, self.A_DAY_STATE.next_substate)
        # Input the encounter stage number, go to the stage and open door
        self.A_DAY_STATE.exec(None, [FloorSelected(A_STAGE_SRC)])
        self.wait_for_animation_assert_state(self.A_DAY_STATE.open_door)

        # open_door animate, client walk to elevator anime, greeting, close_door animation and dialogue
        self.wait_for_animation_assert_state(self.A_DAY_STATE.encounter_enter_elevator)
        self.wait_for_animation_assert_state(self.A_DAY_STATE.greet_encounter)
        self.wait_for_dialog_assert_state(self.A_DAY_STATE.close_door)
        self.wait_for_animation_assert_state(self.A_DAY_STATE.dialog_with_encounter)
        self.wait_for_dialog_assert_state(self.A_DAY_STATE.wait_for_player_input_with_encounter)

        # Press right button and go to the right elevator stage and farawell
        self.A_DAY_STATE.exec(None, [FloorSelected(A_STAGE_DEST)])
        self.wait_for_animation_assert_state(self.A_DAY_STATE.reach_dest)
        self.wait_for_dialog_assert_state(self.A_DAY_STATE.open_door_encounter_leave)
