#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    If a ValueError message is caught, a corresponding
    message is printed to standard error.


    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return True
        
    except (ValueError, TypeError) as error:
        print("Exception {}".format(error), file = sys.stderr)
        return False
        

