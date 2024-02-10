#!/usr/bin/python3
"""Base Geometry class"""


class BaseGeometry:
    """The base class for geometry shapes
        defines area function
    """
    def area(self):
        raise Exception("area() is not implemented")
