#!/usr/bin/python3
"""
module that has the square class
"""
Rectangle = __import('9-rectangle').Rectangle


def Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """
        constructor of square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ calc area of square """
        return self.__size * self.__size
