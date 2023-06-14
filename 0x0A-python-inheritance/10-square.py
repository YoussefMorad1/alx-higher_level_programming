#!/usr/bin/python3
"""
square module
"""
Rectangle = __import('9-rectangle').Rectangle


def Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return size * size
