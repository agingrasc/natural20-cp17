import unittest
from domain.state.daystate import DayState
from domain.clients import ClientBuilder, Clients
from domain.days import *

class DayStateTest(unittest.TestCase):
    A_DAY = 1
    def setUp(self):
        self.A_CLIENT = ClientBuilder().with_days([self.A_DAY]).build()

    def tearDown(self):
        pass

    def test_given_a_client_when_exec_then_a_client_is_current_client(self):
        day = Day(self.A_DAY, clients=Clients([self.A_CLIENT]), load_from_json=False, nb_encounter=1)
        day_state = DayState(day)

        day_state.exec()

        self.assertEqual(self.A_CLIENT, day_state.current_client)

