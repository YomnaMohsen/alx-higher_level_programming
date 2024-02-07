#!/usr/bin/python3

"""add args to list and save to file"""


import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
file_name = "add_item.json"

try:
    obj = load_from_json_file(file_name)
    obj.extend(sys.argv[1:])
    save_to_json_file(obj, file_name)

except FileNotFoundError:
    save_to_json_file(sys.argv[1:], file_name)
