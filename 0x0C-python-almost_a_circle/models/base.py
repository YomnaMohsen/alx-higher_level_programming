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
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of
        list_objs to a file

        Args:
        cls : reference to class
        list_objs :list of objects
        """
        filename = cls.__name__ + ".json"
        list_dict = []
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                for obj in list_objs:
                    dict = obj.to_dictionary()
                    list_dict.append(dict)
                file.write(cls.to_json_string(list_dict))
