#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """deletes keys with a specific value in a dictionary."""
    while value in a_dictionary.values():
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break
    return a_dictionary        
# we can't delete item from dict while iterating it 