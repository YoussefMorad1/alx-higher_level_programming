#!/usr/bin/python3
"""
base geometry module
"""


class BaseGeometry:
    """ Base Geometry Class """
    def area(self):
        """
        area function
        """
        raise Exception("area() is not implemented")
    
    def integer_vaildator(self, name, value):
        if type(value) != int:
            raise TypeError("{name} must be an integer")
        if value <= 0:
            raise ValueError("{name} must be greater than 0")
