#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ function that adds all unique 
    integers in a list (only once for each integer)."""
    sum = 0
    
    for x in set(my_list):
        sum += x
    return sum
