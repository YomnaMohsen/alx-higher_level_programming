#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ prints a dictionary by ordered keys"""
    for k in sorted(a_dictionary):# sorted ret list of sorted keys
        print("{:s}: {}".format(k, a_dictionary[k]))
