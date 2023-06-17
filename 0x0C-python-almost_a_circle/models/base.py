#!/usr/bin/python3
"""
this module has the base class
"""
import json


class Base:
    """
    Base class to manage IDs
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor of the Base class
        """
        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dic):
        if list_dic is None or len(list_dic) == 0:
            return "[]"
        strr = json.dumps(list_dic)
        return strr

    @classmethod
    def save_to_file(cls, list_objs):
        list_dics = []
        if list_objs is None:
            list_objs = []
        for element in list_objs:
            list_dics.append(element.to_dictionary())
        str_to_save = cls.to_json_string(list_dics)
        with open(cls.__name__ + '.json', 'w', encoding='UTF-8') as f:
            f.write(str_to_save)
