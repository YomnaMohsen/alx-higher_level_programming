#!/usr/bin/python3
"""
    Defines print square function
"""


def print_square(size):
    """
    prints a square with the character #

    Args:
        size (int): length of square
    Raise TypeError:
      if size not int
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
