#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        for j in range(len(lists)):
            print("{:d}".format(lists[j]), end=" ")
        print("")
