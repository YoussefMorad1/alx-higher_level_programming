#!/usr/bin/python3
"""
this module prints square matrix
"""


def print_square(size):
    """
    print square with character '#'
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for _ in range(size):
        for __ in range(size):
            print('#', end='')
        print()
