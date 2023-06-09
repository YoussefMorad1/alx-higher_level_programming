#!/usr/bin/python3
"""
This Module has matrix division functions
"""


def matrix_divided(mat, div):
    if type(mat) != list or type(mat[0]) != list or \
            [type(x) in (int, float) for row in mat for x in row].count(True) != len(mat) * len(mat[0]):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if [len(row) for row in mat].count(len(mat[0])) != len(mat):
        raise TypeError('Each row of the matrix must have the same size')
    if type(div) not in (int, float) or div != div or div == div + 1:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    mat2 = list()
    for i in range(len(mat)):
        mat2.append(mat[i][:])
        for j in range(len(mat[i])):
            mat2[i][j] = round(mat[i][j] / div, 2)
    return mat2
