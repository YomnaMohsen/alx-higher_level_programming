#!/usr/bin/python3
"""Base Geometry class"""


class BaseGeometry:
    """The base class for geometry shapes
        defines area function
    """
    def area(self):
        """raise not-implemented exception"""
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """validate int value
            Args:
            name :string
            value: int
        """
        
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
