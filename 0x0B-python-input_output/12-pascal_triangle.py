#!/usr/bin/python3
""" module important much """


def pascal_triangle(n):
    if n <= 0:
        return []
    l = [[0 for x in range(n)] for y in range(n)]

