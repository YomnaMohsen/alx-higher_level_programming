#!/usr/bin/python3
"""Base class module"""

import json


class Base:
    """Base class for all subclasses"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries
        Args : list of dictionaries (list)
        """
        if list_dictionaries is None or list_dictionaries == []:
            return None
        return json.dumps(list_dictionaries)
