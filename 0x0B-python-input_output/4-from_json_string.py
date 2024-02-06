#!/usr/bin/python3

"""define from_json_string function"""

import json


def from_json_string(my_str):
    """
    return object represenation
    represented by json string
    Args:
        my_str : json string
    """

    return json.loads(my_str)
