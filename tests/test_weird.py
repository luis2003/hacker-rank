import unittest
from .context import weird


class WeirdTestCase(unittest.TestCase):
    def test_odd_is_weird(self):
        # Arrange
        input_value = 3
        expected_output = "Weird"

        # Act
        actual_output = weird.determine_weirdness(input_value)

        # Assert
        self.assertEqual(expected_output, actual_output)

    def test_even_two_to_five_not_weird(self):
        input_value = 2
        expected_output = "Not Weird"

        actual_output = weird.determine_weirdness(input_value)

        self.assertEqual(expected_output, actual_output)

    def test_even_six_to_twenty_is_weird(self):
        input_value = 6
        expected_output = "Weird"

        actual_output = weird.determine_weirdness(input_value)

        self.assertEqual(expected_output, actual_output)

    def test_even_greater_than_twenty_not_weird(self):
        input_value = 22
        expected_output = "Not Weird"

        actual_output = weird.determine_weirdness(input_value)

        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
