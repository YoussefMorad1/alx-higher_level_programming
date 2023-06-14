#!/usr/bin/python3
""" module new """


def is_kind_of_class(obj, a_class):
    """ 
    Checks if the object is an instance of the specified class 
    or from one of it's subclasses 
    """
    return isinstance(obj, a_class)
