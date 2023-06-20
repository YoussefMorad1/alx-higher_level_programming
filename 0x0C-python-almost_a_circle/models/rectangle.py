#!/usr/bin/python3
"""This Module has Rectangle Class
"""
import models.base as base


class Rectangle(base.Base):
    """Rectangle Class that really loves you
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) != int:
            raise TypeError('width must be an integer')
        if val <= 0:
            raise ValueError('width must be > 0')
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) != int:
            raise TypeError('height must be an integer')
        if val <= 0:
            raise ValueError('height must be > 0')
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) != int:
            raise TypeError('x must be an integer')
        if val < 0:
            raise ValueError('x must be >= 0')
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) != int:
            raise TypeError('y must be an integer')
        if val < 0:
            raise ValueError('y must be >= 0')
        self.__y = val

    def update(self, *args, **kwargs):
        """update attributes of the instance
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if len(args) > 0:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, val in kwargs.items():
                if key in attributes:
                    setattr(self, key, val)

    def area(self):
        """return area of the rectangle
        """
        return self.height * self.width

    def display(self):
        """display the rectangle with '#' in stdout
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x, end='')
            for __ in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """return str reperesentation of rectangle
        """
        return f'[Rectangle] ({self.id}) ' +\
        f'{self.x}/{self.y} - {self.width}/{self.height}'

    def to_dictionary(self):
        """return a dictionary with each attribute as key
        and related to its value
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        dic = {}
        for att in attributes:
            dic[att] = getattr(self, att)
        return dic
