import unittest
import source.loop as loop

class LoopTestCase(unittest.TestCase):
    def test_input_3(self):
        input_value = 3
        expected_output = [0, 1, 4]

        actual_output = loop.get_previous_squares(input_value)

        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
