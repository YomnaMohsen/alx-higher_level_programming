#!/usr/bin/python3
import json
"""define to_json_string function"""


def to_json_string(my_obj):
    """
    return json represenation of
    string object
    Args:
        my_obj : python object
    """
    return json.dumps(my_obj)
