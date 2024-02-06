#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """read_file
       Args:
       filename: string
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
        print()
