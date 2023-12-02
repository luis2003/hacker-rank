def determine_weirdness(input_value: int):
    if _is_even(input_value):
        return "Weird"
    elif _in_six_to_twenty_inclusive_range(input_value):
        return "Weird"
    elif _is_greater_than_twenty(input_value):
        return "Not Weird"
    else:
        return "Not Weird"


def _is_even(value: int) -> bool:
    if value % 2 != 0:
        return True
    return False


def _in_six_to_twenty_inclusive_range(value: int) -> bool:
    if 6 <= value <= 20:
        return True
    return False


def _is_greater_than_twenty(value: int) -> bool:
    if value > 20:
        return True
    return False