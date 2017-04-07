import unittest
from domain.state.daystate import DayState
from domain.encounter import EncounterBuilder, Encounter
from domain.day import *

class DayTest(unittest.TestCase):
    A_DAY = 1
    def setUp(self):
        FLAG_A = 'lol'
        self.A_TRIGGABLE_ENCOUNTER = EncounterBuilder().build()
        self.A_UNTRIGGABLE_ENCOUNTER = EncounterBuilder().with_include([FLAG_A]).build()

    def tearDown(self):
        pass

    def test_given_no_encounter_when_pop_encounter_then_return_None(self):
        day = Day(self.A_DAY, load_from_json=False, encounters=[])

        self.assertIsNone(day.pop_triggable_encounter([]))

    def test_given_a_day_with_a_triggerable_encounter_when_pop_encounter_then_return_that_encounter(self):
        day = Day(self.A_DAY, load_from_json=False, encounters=[self.A_TRIGGABLE_ENCOUNTER])

        self.assertEqual(self.A_TRIGGABLE_ENCOUNTER, day.pop_triggable_encounter([]))

    def test_given_a_day_with_a_untriggerable_encounter_when_pop_encounter_then_return_none(self):
        day = Day(self.A_DAY, load_from_json=False, encounters=[self.A_UNTRIGGABLE_ENCOUNTER])

        self.assertEqual(None, day.pop_triggable_encounter([]))


    def test_given_a_day_with_a_untriggable_encounter_and_a_triggable_when_pop_encounter_then_return_none(self):
        day = Day(self.A_DAY, load_from_json=False, encounters=[self.A_UNTRIGGABLE_ENCOUNTER, self.A_TRIGGABLE_ENCOUNTER])

        self.assertEqual(self.A_TRIGGABLE_ENCOUNTER, day.pop_triggable_encounter([]))


