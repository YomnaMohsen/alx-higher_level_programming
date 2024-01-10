#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = [[x**2 for x in l_items] for l_items in matrix]
    return new_mat
