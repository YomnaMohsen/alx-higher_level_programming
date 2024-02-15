#!/usr/bin/python3
"""Base class module"""


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
    #@staticmethod        
    #def to_json_string(list_dictionaries):        
