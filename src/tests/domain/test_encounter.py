import unittest

from domain.encounter import *

class EncounterTest(unittest.TestCase):
    def setUp(self):
        pass
        #self.A_CLIENT_DAY1 =  ClientBuilder().with_days([self.DAY1]).build()
        #self.A_CLIENT_DAY2 =  ClientBuilder().with_days([self.DAY2]).build()
        #self.TWO_CLIENTS = [self.A_CLIENT_DAY1, self.A_CLIENT_DAY1]

    def tearDown(self):
        pass

    def test_given_a_encounter_with_a_greeting_when_say_greeding_then_a_greeding_is_returned(self):
        A_GREEDING = "hello"
        A_FAREWELL = "bye"
        A_INSULT = "FU"
        A_DIALOG = "so"
        encounter = EncounterBuilder().with_greeting([A_GREEDING])\
                                      .with_farewell([A_FAREWELL])\
                                      .with_insult([A_INSULT])\
                                      .with_dialog([A_DIALOG]).build()

        self.assertEqual(A_GREEDING, encounter.say_greeting())
        self.assertEqual(A_FAREWELL, encounter.say_farewell())
        self.assertEqual(A_INSULT, encounter.say_insult())
        self.assertEqual([A_DIALOG], encounter.dialogs)

    def test_given_a_encounter_that_include_flag_A_when_check_trigger_with_flag_A_then_encounter_triggered(self):
        FLAG_A = "steve_dead"
        encounter = EncounterBuilder().with_include([FLAG_A]).build()

        self.assertTrue(encounter.is_encounter_trigger([FLAG_A]))


    def test_given_a_encounter_that_include_flag_A_when_check_trigger_without_flag_A_then_encounter_not_triggered(self):
        FLAG_A = "steve_dead"
        encounter = EncounterBuilder().with_include([FLAG_A]).build()

        self.assertFalse(encounter.is_encounter_trigger([]))


    def test_given_a_encounter_that_exlude_flag_A_when_check_trigger_with_flag_A_then_encounter_not_triggered(self):
        FLAG_A = "steve_dead"
        encounter = EncounterBuilder().with_exclude([FLAG_A]).build()

        self.assertFalse(encounter.is_encounter_trigger([FLAG_A]))
