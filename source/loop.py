from typing import List

MIN_INPUT_VALUE = 1
MAX_INPUT_VALUE = 20


def calculate_previous_squares(input_value: int) -> List[int]:
    """
    Return a list with the calculated squares of all non-negative integers less than the input value

    :param input_value: an integer (MIN_INPUT_VALUE <= input_value <= MAX_INPUT_VALUE)
    :return: a list containing the squares of all non-negative integers less than input
    """
    if input_value > MAX_INPUT_VALUE or input_value < MIN_INPUT_VALUE:
        raise ValueError(f"input value must be between {MIN_INPUT_VALUE} and {MAX_INPUT_VALUE}")
    return [index * index for index in range(input_value)]


def print_previous_squares(squares: List[int]) -> None:
    """print each value in a separate line """
    print('\n'.join(map(str, squares)))


def main() -> None:
    try:
        n = int(input(f"Enter an integer between {MIN_INPUT_VALUE} and {MAX_INPUT_VALUE}: "))
        squares = calculate_previous_squares(n)
        print_previous_squares(squares)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
