#!/usr/bin/python3
"""
This Module has matrix division functions
"""


def matrix_divided(mat, div):
    if [len(row) for row in mat].count(len(mat[0])) != len(mat):
        raise TypeError('Each row of the matrix must have the same size')
    if [type(x) in (int, float) for row in mat for x in row].count(True) != len(mat) * len(mat[0]):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if type(div) not in (int, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    mat2 = mat.copy()
    for row in mat2:
        for i in range(len(row)):
            row[i] = round(row[i] / div, 2)
    return mat2
