#!/usr/bin/python3

"""define save_to_json_file function"""

import json


def save_to_json_file(my_obj, filename):
    """
    write obj to text file in
    json rep.
    Args:
        my_obj : python object
        filename: string file name
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
