#!/usr/bin/python3
"""write file module"""


def write_file(filename="", text=""):
    """write_file
       Args:
       filename: string
       text: string
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
