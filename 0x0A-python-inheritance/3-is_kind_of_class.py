#!/usr/bin/python3
"""Define is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is  an instance of, or if the object 
    is an instance of a class that inherited from
    otherwise False
    Args:
        obj (any object type)
        a_class certain class to compare with
    """
    return isinstance(obj, a_class)
