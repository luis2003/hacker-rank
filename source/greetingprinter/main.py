class GreetingPrinter:

    def print_two_part_greeting(self, *greeting_parts: tuple):
        print(greeting_parts[0], greeting_parts[1], sep=", ", end="!")


if __name__ == '__main__':

    greeting_str_part1 = "Hello"
    greeting_str_part2 = "World"
    a_greeting_printer = GreetingPrinter()
    a_greeting_printer.print_two_part_greeting(greeting_str_part1, greeting_str_part2)

