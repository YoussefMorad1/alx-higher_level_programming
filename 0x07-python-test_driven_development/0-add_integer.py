#!/usr/bin/python3
"""
This module has the add integer functions
"""


def add_integer(a, b=98):
    """
    This function adds to integers
    """
    if type(a) not in (int, float) or a == a + 1 or a != a:
        raise TypeError('a must be an integer')
    if type(b) not in (int, float) or b == b + 1 or b != b:
        raise TypeError('b must be an integer')
    return int(a) + int(b)

