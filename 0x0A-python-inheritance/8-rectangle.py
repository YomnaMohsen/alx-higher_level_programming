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
        super().__width = width
        super().__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
