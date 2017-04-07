import unittest

from util import dialog


class TestDialog(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_given_a_dialog_that_is_smaller_that_the_column_limit_when_break_dialog_line_then_return_unchanged_dialog(self):
        dialog_lines = "Hello, world!"
        broked_dialog_lines = dialog.break_dialog_lines(dialog_lines)
        self.assertEqual([dialog_lines], broked_dialog_lines)

    def test_given_a_dialog_with_a_new_line_that_is_smaller_that_the_column_limit_when_break_dialog_line_then_return_two_lines(self):
        dialog_lines = "Hello\nWorld!"
        broked_dialog_lines = dialog.break_dialog_lines(dialog_lines)
        self.assertEqual(2, len(broked_dialog_lines))

    def test_given_a_dialog_longer_that_the_column_limit_when_break_dialog_line_then_return_two_lines(self):
        dialog_lines = "a" * (int(dialog.LINE_COL_LIMIT/2)) + " " + "b" * (int(dialog.LINE_COL_LIMIT/2) + 5)
        broked_dialog_lines = dialog.break_dialog_lines(dialog_lines)
        self.assertEqual(2, len(broked_dialog_lines))

    def test_given_a_dialog_with_a_new_line_and_the_subline_is_longer_that_the_column_limit_when_break_dialog_line_then_return_three_lines(self):
        dialog_lines = "a" * (int(dialog.LINE_COL_LIMIT/2)) + "\n" + "b" * (int(dialog.LINE_COL_LIMIT/4)) + " " + "c" * dialog.LINE_COL_LIMIT
        broked_dialog_lines = dialog.break_dialog_lines(dialog_lines)
        self.assertEqual(3, len(broked_dialog_lines))
