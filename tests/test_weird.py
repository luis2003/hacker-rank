import unittest
from .base_test_stdout import BaseTestStdout
from .context import weird


class WeirdTestCase(BaseTestStdout):
    def test_odd_is_weird(self):
        # Arrange
        input_value = 3
        expected_output = "Weird"

        # Act
        result = weird.determine_weirdness(input_value)

        # Assert
        self.assertEqual(result, expected_output)

    def test_even_two_to_five_not_weird(self):
        input_value = 2
        expected_output = "Not Weird"

        result = weird.determine_weirdness(input_value)

        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
