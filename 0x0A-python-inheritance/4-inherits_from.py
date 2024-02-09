#!/usr/bin/python3
"""Define inherits_from module"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of,  a class that inherited
    (directly or indirectly) from the specified class
    otherwise False
    Args:
        obj (any object type)
        a_class certain class to compare with
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
