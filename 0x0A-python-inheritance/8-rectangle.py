#!/usr/bin/python3
""" rectangle module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

def Rectangle(BaseGeometry):
    """
    Rectangle Class
    """
    def __init__(self, width, height):
        """
        constructor of rectangle
        """
        self.integer_validator("width", width)
        self.integer_vaildator("height", height)
        self.__height = height
        self.__width = width
