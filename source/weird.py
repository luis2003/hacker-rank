def determine_weirdness(input_value: int):
    if _is_odd(input_value):
        print("Weird")
    elif _in_six_to_twenty_inclusive_range(input_value):
        print("Weird")
    elif _is_greater_than_twenty(input_value):
        print("Not Weird")
    else:
        print("Not Weird")


def _is_odd(value: int) -> bool:
    return value % 2 != 0


def _in_six_to_twenty_inclusive_range(value: int) -> bool:
    return 6 <= value <= 20


def _is_greater_than_twenty(value: int) -> bool:
    return value > 20

