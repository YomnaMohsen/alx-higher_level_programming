#!/usr/bin/python3

"""define load_from_json_file function"""

import json


def load_from_json_file(filename):
    """
    creates obj from json file
    Args:
        filename: string file name
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
