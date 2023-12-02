import unittest
import sys
from io import StringIO
from source.greetingprinter.main import GreetingPrinter


class TestGreetingPrinter(unittest.TestCase):
    def setUp(self):
        self.original_stdout = sys.stdout
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self) -> None:
        sys.stdout = self.original_stdout

    def test_print_two_part_greeting(self):
        # Arrange
        greeting_str_part1 = "Hello"
        greeting_str_part2 = "World"
        expected_output = "Hello, World!"

        # Act
        a_greeting_printer = GreetingPrinter()
        a_greeting_printer.print_two_part_greeting(greeting_str_part1, greeting_str_part2)

        self.assertEqual(self.held_output.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
