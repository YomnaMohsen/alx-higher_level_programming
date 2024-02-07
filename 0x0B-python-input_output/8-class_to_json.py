#!/usr/bin/python3
"""defines class_to_json function"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    Args:
        obj: class instance
    """
    return obj.__dict__
