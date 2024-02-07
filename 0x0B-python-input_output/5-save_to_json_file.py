#!/usr/bin/python3

"""define save_to_json_file function"""

import json


def save_to_json_file(my_obj, filename):
    """
    write obj to text file in
    json rep.
    Args:
        my_obj : python object
        filename: string file name
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
