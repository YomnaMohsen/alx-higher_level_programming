#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        for m in lists:
            print("{:d}".format(m), end=" " if j != len(lists) - 1 else "")
        print("")
