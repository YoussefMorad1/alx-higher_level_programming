#!/usr/bin/python3
""" rectangle module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle Class
    """
    def __init__(self, width, height):
        """
        constructor of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """
        area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
