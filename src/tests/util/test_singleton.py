import unittest

from util.singleton import Singleton


class MockSingleton(metaclass=Singleton):
    def __init__(self):
        self.first_field = 0
        self.second_field = 0


class SingletonTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_given_a_singleton_when_creating_new_singleton_return_same_reference(self):
        first_singleton = MockSingleton()
        second_singleton = MockSingleton()
        self.assertTrue(first_singleton is second_singleton)

    def test_given_a_singleton_when_creating_new_singleton_return_same_first_field_value(self):
        first_singleton = MockSingleton()
        second_singleton = MockSingleton()
        self.assertEqual(first_singleton, second_singleton)
        first_singleton.first_field = 1
        self.assertEqual(first_singleton, second_singleton)
        second_singleton.first_field = 2
        self.assertEqual(first_singleton, second_singleton)