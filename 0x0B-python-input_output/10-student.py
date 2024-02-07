#!/usr/bin/python3
"""Rectangle class"""


class Student:
    """This class defines student data"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student object.
        Args:
            firs_name (string): set student 1st name
            last_name (string): set student last name
            age (int): set student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
        retrieves a dictionary representation of
        a Student instance based on condition

        Args:
            attr: generic type, optional
        """
        if attr is None:
            return self.__dict__
        dict_s = {}
        for arg in attr:
            val = self.__dict__.get(arg)
            if val:
                dict_s[arg] = val
        return dict_s
