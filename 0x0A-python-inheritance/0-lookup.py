#!/usr/bin/python3
"""
python module lookup function
"""


def lookup(obj):
    """
    return list of avaiable attributes and methods in obj
    """
    return dir(obj)
