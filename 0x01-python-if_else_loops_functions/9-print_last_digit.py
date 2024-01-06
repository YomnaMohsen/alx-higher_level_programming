#!/usr/bin/python3
def print_last_digit(number):
    number = number - (10 * int(number / 10))
    if number < 0:
        number = -number
    print("{:d}".format(number), end="")
    return number
