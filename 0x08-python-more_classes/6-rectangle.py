#!/usr/bin/python3
"""
This module is for having Rectangle Class
"""


class Rectangle:
    """
    class represents a rectangle
    """
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) == int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2\
            if self.width > 0 and self.height > 0 else 0

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        for i in range(self.height):
            rectangle += "#" * self.width + \
                ("\n" if i < self.height - 1 else "")
        return rectangle

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
