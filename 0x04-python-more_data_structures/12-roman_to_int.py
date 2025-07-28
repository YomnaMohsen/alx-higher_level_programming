#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    dict = {"I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000}
    if not (isinstance(roman_string, str)) or roman_string is None:
        return 0
   
    for i in range(len(roman_string)):
        if i + 1 < len(roman_string) and dict[roman_string[i]] < dict[roman_string[i + 1]]:
            sum -= dict[roman_string[i]]
        else:
            sum += dict[roman_string[i]]
    return sum           
