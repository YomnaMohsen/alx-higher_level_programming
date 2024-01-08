#!/usr/bin/python3
def multiple_returns(sentence):
    first = ''
    length = 0
    if sentence[0] == " ":
        first = None
    else:
        first = sentence[0]
    return len(sentence), first
