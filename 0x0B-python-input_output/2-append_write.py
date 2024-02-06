#!/usr/bin/python3
"""append_write module"""


def append_write(filename="", text=""):
    """append to file string text
       Args:
       filename: string
       text: string
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
