import unittest
from .base_test_stdout import BaseTestStdout
from .context import weird

class WeirdTestCase(BaseTestStdout):
    def test_determine_weirdness_odd(self):
        input = 3
        expected_output = "Weird"
        result = weird.determine_weirdness(input)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
