#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":
    list_output = Rectangle.from_json_string('[{ "id": 89 }]')
    print("[{}] {}".format(type(list_output), list_output))