#!/usr/bin/python3
"""Defines MyInt that is subclass from int"""


class MyInt(int):
    """Class MYInt"""
    def __eq__(self, other):
        return int.__ne__(self, other)
    
    def __ne__(self, other):
        return int.__eq__(self, other)