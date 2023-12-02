import unittest
from .context import greetingprinter
from .base_test_stdout import BaseTestStdout


class TestGreetingPrinter(BaseTestStdout):

    def test_print_two_part_greeting(self):
        # Arrange
        greeting_str_part1 = "Hello"
        greeting_str_part2 = "World"
        expected_output = "Hello, World!"

        # Act
        a_greeting_printer = greetingprinter.GreetingPrinter()
        a_greeting_printer.print_two_part_greeting(greeting_str_part1, greeting_str_part2)

        self.assertEqual(self.held_output.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
