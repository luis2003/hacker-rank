from typing import List


def calculate_previous_squares(input_value: int) -> List[int]:
    """
    Return a list with the calculated squares of all non-negative integers less than the input value

    :param input_value: an integer
    :return: a list containing the squares of all non-negative integers less than input
    """
    return [index * index for index in range(input_value)]


def print_previous_squares(input_value: int) -> None:
    """print each value in separate line """
    for value in calculate_previous_squares(input_value):
        print(value)

