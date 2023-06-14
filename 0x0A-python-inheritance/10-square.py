#!/usr/bin/python3
""" rectangle module """
Rectangle = __import__('9-rectangle').Rectangle


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
