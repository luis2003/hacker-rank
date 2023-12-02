def determine_weirdness(input_value: int):
    if _is_even(input_value):
        return "Weird"
    else:
        return "Not Weird"


def _is_even(value: int) -> bool:
    if value % 2 != 0:
        return True
    return False
