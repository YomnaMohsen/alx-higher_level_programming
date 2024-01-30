#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """This class defines a rectangle shape"""
    def __init__(self, width=0, height=0):
        """Initializes a rectangle object.
        Args:
            width (int): set rectangle width
            height(int): set rectangle height

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Return width"""
        return self.__width

    @property
    def height(self):
        """Return height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates area"""
        return self.__height * self.__width

    def perimeter(self):
        """calculates perimter"""
        if (self.__height == 0 or self.__width == 0):
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """custom str fn"""
        if self.height == 0 or self.width == 0:
            return ""
        s = ("#" * self.width + "\n") * (self.height - 1) + ("#" * self.width)
        return s
