import unittest
from .base_test_stdout import BaseTestStdout
from .context import weird


class WeirdTestCase(BaseTestStdout):
    def test_odd_is_weird(self):
        # Arrange
        input_value = 3
        expected_output = "Weird"

        # Act
        weird.determine_weirdness(input_value)

        # Assert
        self.assertEqual(expected_output, self.held_output.getvalue().rstrip())

    def test_even_two_to_five_not_weird(self):
        input_value = 2
        expected_output = "Not Weird"

        weird.determine_weirdness(input_value)

        self.assertEqual(expected_output, self.held_output.getvalue().rstrip())

    def test_even_six_to_twenty_is_weird(self):
        input_value = 6
        expected_output = "Weird"

        weird.determine_weirdness(input_value)

        self.assertEqual(expected_output, self.held_output.getvalue().rstrip())

    def test_even_greater_than_twenty_not_weird(self):
        input_value = 22
        expected_output = "Not Weird"

        weird.determine_weirdness(input_value)

        self.assertEqual(expected_output, self.held_output.getvalue().rstrip())


if __name__ == '__main__':
    unittest.main()
