import unittest

from domain.days import *

class ClientsTest(unittest.TestCase):
    DAY1 = 1
    DAY2 = 2
    def setUp(self):
        self.A_CLIENT_DAY1 =  Client({
            "id": "Steve",
            "days": [1],
            "greeting": "hello",
            "farewell": "bye",
            "tips_min": 1,
            "tips_max": 3
        })
        self.A_CLIENT_DAY2 =  Client({
            "id": "Steve",
            "days": [2],
            "greeting": "hello",
            "farewell": "bye",
            "tips_min": 1,
            "tips_max": 3
        })
        self.TWO_CLIENTS = [self.A_CLIENT_DAY1, self.A_CLIENT_DAY1]

    def tearDown(self):
        pass

    def test_given_a_client_day1_when_pick_one_client_for_day1_return_a_client(self):
        clients = Clients([self.A_CLIENT_DAY1])

        self.assertEqual([self.A_CLIENT_DAY1], clients.pick_client(self.DAY1, 1))

    def test_given_two_clients_when_pick_one_client_for_day2_return_one_client(self):
        clients = Clients([self.A_CLIENT_DAY1, self.A_CLIENT_DAY2])

        self.assertEqual([self.A_CLIENT_DAY2], clients.pick_client(self.DAY2, 1))

    def test_given_two_clients_day1_when_pick_one_client_return_one_client(self):
        clients = Clients(self.TWO_CLIENTS)

        self.assertEqual(1, len(clients.pick_client(self.DAY1, 1)))

    def test_given_no_client_when_pick_one_client_return_exception(self):
        NO_CLIENT = []
        clients = Clients(NO_CLIENT)
        with self.assertRaises(Exception):
            clients.pick_client(self.DAY1, 1)
