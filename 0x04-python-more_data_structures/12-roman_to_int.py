#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    dict = {"I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000}
    sub = ["IV", "IX", "XL", "XC", "CD", "CM"]
    sub_st = " "
    if not (isinstance(roman_string, str)) or roman_string is None:
        return 0
    i = 0
    while (i < len(roman_string)):
        if (i == (len(roman_string) - 1)):
            sum += dict[roman_string[i]]
            break
        sub_st = roman_string[i] + roman_string[i + 1]
        if is_sub(sub, sub_st):
            sum += dict[roman_string[i + 1]] - dict[roman_string[i]]
            i += 2
        else:
            sum += dict[roman_string[i]]
            i += 1
        return sum


def is_sub(s, s2):
    if (s2 in s):
        return True
    return False

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))