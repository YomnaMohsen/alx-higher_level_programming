#!/usr/bin/python3
"""Square class"""


class Square:
    """This class defines a square shape"""
    def __init__(self, size=0):
        """Initializes a square object.
        Args:
            size (int): set square size

        """
        self.size = size

    @property
    def size(self):
        """Rteurn size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the square area"""
        return self.__size * self.__size
