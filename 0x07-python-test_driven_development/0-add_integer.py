#!/usr/bin/python3
"""add integer module

"""


def add_integer(a, b=98):
    """Return the addition of 2 int (a + b)
    Args:
        a: int number
        b: int number
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    max = (2 ** 31) - 1
    min = -max - 1
    if a > max or a < min or b > max or b < min:
        raise OverflowError("integer overflow")
    return int(a) + int(b)
