#!/usr/bin/python3
"""Define is_same_class module"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of
    the specified class ; otherwise False
    Args:
        obj (any object type)
        a_class certain class to compare with
    """
    return type(obj) == a_class
