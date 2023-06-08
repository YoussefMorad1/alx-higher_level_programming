#!/usr/bin/python3
"""
This module is for having Rectangle Class
"""


class Rectangle:
    """
    class represents a rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError
        else:
            raise TypeError

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self):
        if type(value) == int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError
        else:
            raise TypeError
