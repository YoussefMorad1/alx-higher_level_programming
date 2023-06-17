#!/usr/bin/python3
"""
this module has the base class
"""


class Base:
    """
    Base class to manage IDs
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor of the Base class
        """
        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_objects
