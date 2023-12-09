import unittest
import source.loop as loop
from base_test_stdout import BaseTestStdout


class LoopPrintingTestCase(BaseTestStdout):
    def test_print_input_3(self):
        input_value = 3
        expected_output = "0\n1\n4\n"

        loop.print_previous_squares(input_value)

        self.assertEqual(self.held_output.getvalue(), expected_output)


class LoopTestCase(unittest.TestCase):
    def test_input_3(self):
        input_value = 3
        expected_output = [0, 1, 4]

        actual_output = loop.calculate_previous_squares(input_value)

        self.assertEqual(actual_output, expected_output)

    def test_input_5(self):
        input_value = 5
        expected_output = [0, 1, 4, 9, 16]

        actual_output = loop.calculate_previous_squares(input_value)

        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
