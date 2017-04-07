import unittest

from display.button import Button
from util.geometry import Vector


class TestButton(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_given_button_when_pos_is_inside_return_true(self):
        button = Button(Vector(100, 100), Vector(25, 25))
        pos = Vector(105, 105)
        self.assertTrue(button.is_inside(pos))