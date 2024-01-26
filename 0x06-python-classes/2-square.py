#!/usr/bin/python3
"""Square class"""


class Square:
    """This class defines a square shape"""
    def __init__(self, size=0):
        """Initializes a square object.
        Args:
            size (int): set square size

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
