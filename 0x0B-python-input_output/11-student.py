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
        dic = dict(vars(self))
        keys = list(dic.keys())
        for key in keys:
            if att is not None and key not in att:
                del dic[key]
        return dic

    def reload_from_json(self, json):
        """ reload from json """ 
        for key in json.keys():
            setattr(self, key, json[key])
