def determine_weirdness(input_value: int) -> str:
    """
        Determine whether the given input value is weird or not.
        Returns "Weird" if the value is odd or in the range [6, 20], otherwise "Not Weird".
    """
    if _is_odd(input_value) or _is_in_six_to_twenty_range(input_value):
        return "Weird"
    else:
        return "Not Weird"


def _is_odd(value: int) -> bool:
    """
    Check if the given value is odd.
    """
    return value % 2 != 0


def _is_in_six_to_twenty_range(value: int) -> bool:
    """
    Check if the given value is in the range [6, 20].
    """
    return 6 <= value <= 20


if __name__ == '__main__':
    print(determine_weirdness(int(input("enter an integer value: "))))
