#!/usr/bin/python3
"""
This module says 'say my name'
"""


def say_my_name(fname, lname=""):
    """
    say my name function
    """
    if type(fname) != str:
        raise TypeError('first_name must be a string')
    if type(lname) != str:
        raise TypeError('last_name must be a string')
    print(f'My name is {fname} {lname}')
