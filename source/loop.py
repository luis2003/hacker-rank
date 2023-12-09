def get_previous_squares(input_value: int) -> list:
    """
    calculate the squares of all non-negative integers less than the input value
    :param input_value: an integer
    :return: a list containing the squares of all non-negative integers less than input
    """
    return [index * index for index in range(input_value)]


def print_previous_squares(input_value: int) -> None:
    """print each value in separate line """
    for value in get_previous_squares(input_value):
        print(value)

