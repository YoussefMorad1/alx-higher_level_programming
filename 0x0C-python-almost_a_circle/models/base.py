#!/usr/bin/python3
""" This module loves you """
import json


class Base:
    """
    Base class to handle IDs
    """
    __nb_objects = 0

    def __init__(self, id=None):
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

    @staticmethod
    def from_json_string(json_str):
        if json_str is None or len(json_str) == 0:
            return []
        return json.loads(json_str)

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

    @classmethod
    def create(cls, **dict):
        obj = None
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 2)
        elif cls.__name__ == 'Square':
            obj = cls(1)
        else:
            obj = cls()
        obj.update(**dict)
        return obj

    @classmethod
    def load_from_file(cls):
        ans = []
        try:
            with open(cls.__name__ + '.json', 'r', encoding='UTF-8') as file:
                filetxt = file.read()
                list_dict = cls.from_json_string(filetxt)
                for dic in list_dict:
                    ans.append(cls.create(**dic))
        except:
            ans = []
        return ans
