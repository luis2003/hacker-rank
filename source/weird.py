def determine_weirdness(input_value: int):
    if _is_odd(input_value) or _is_in_six_to_twenty_range(input_value):
        print("Weird")
    else:
        print("Not Weird")


def _is_odd(value: int) -> bool:
    return value % 2 != 0


def _is_in_six_to_twenty_range(value: int) -> bool:
    return 6 <= value <= 20


