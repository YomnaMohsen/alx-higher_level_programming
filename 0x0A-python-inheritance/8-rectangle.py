#!/usr/bin/python3
"""Base Geometry class"""

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
