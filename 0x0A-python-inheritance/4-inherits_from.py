#!/usr/bin/python3
""" module new """


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    """
    return issubclass(obj, a_class)
