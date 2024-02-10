#!/usr/bin/python3
"""Rectangle class module"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """The rectangle class that inherits BaseGeometry"""

    def __init__(self, width, height):
        """Initializes rectangle class
            Args:
            width :int
            height: int
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """Calculates area"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
