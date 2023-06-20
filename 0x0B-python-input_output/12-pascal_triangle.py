#!/usr/bin/python3
"""
pascal traingle module
"""
def pascal_triangle(n):
    """
    pascal function returns list of list
    """
    res = []
    for i in range(n):
        res.append([0 for _ in range(i+1)])
    res[0][0] = 1
    for i in range(n-1):
        for j in range(i+1):
            res[i+1][j] += res[i][j]
            if j+1 < n:
                res[i+1][j+1] += res[i][j]
    return res
