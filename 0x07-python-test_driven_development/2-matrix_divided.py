#!/usr/bin/python3
"""
Divide matrix module

"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix: it divides a matrix
    by certain div

    Args:
        matrix: list of list
        div (int/float) : (divisor)
    """
    res_mat = []
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(item, list) for item in matrix)):

        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not all(isinstance(num, (int, float))
               for num in [n for item1 in matrix for n in item1]):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not all(len(item) == len(matrix[0]) for item in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for sub_list in matrix:
        sub_mat = []
        for num in sub_list:
            sub_mat.append(round(num/div, 2))
        res_mat.append(sub_mat)
    return res_mat
