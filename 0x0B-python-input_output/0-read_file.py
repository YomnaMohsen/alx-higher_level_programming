#!/usr/bin/python3
"""Define read_file module"""


def read_file(filename=""):
    """reads from file amd print 
    to stdout
    Args:
    filename: string
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
