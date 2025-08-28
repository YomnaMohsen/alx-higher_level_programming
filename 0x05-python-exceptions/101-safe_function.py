#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    """Returns the result of the function,

        Otherwise, 
        returns None if something happens during the function
        and prints in stderr the error precede by Exception
    """
    try:
        value = fct(*args)
        return value
        
    except:
        print("Exception {}".format(sys.exc_info()[1]), file = sys.stderr)
        return None

def my_div(a, b):
    return a / b

result = safe_function(my_div, 10, 2)
print("result of my_div: {}".format(result))

result = safe_function(my_div, 10, 0)
print("result of my_div: {}".format(result))