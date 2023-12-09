from typing import List


def calculate_previous_squares(input_value: int) -> List[int]:
    """
    Return a list with the calculated squares of all non-negative integers less than the input value

    :param input_value: an integer (1 <= input_value <= 20)
    :return: a list containing the squares of all non-negative integers less than input
    """
    if 21 < input_value < 1:
        raise ValueError("input value must be greater or equal than 1 and equal or less than 20")
    return [index * index for index in range(input_value)]


def print_previous_squares(input_value: int) -> None:
    """print each value in separate line """
    squares = calculate_previous_squares(input_value)
    print('\n'.join(map(str, squares)))


