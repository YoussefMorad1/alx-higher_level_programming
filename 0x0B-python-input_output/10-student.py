#!/usr/bin/python3
""" module module """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """ constructor method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, att=None):
        """ to json method """
        dic = vars(self)
        for key in dic.keys():
            if att is not None and key not in att:
                del dic[key]
        return dic
