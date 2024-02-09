#!/usr/bin/python3
"""Define lookup module"""


def lookup(obj):
    """
    Returns the list of available attributes
    and methods of an object
    Args:
        obj (generic type)
    """
    return (dir(obj))
