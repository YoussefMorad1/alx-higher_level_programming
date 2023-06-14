#!/usr/bin/python3
""" hello module """
import json


def save_to_json_file(my_obj, filename):
    """ save this obj in file as json repersentation """
    with open(filename, 'w', encoding='UTF-8'):
        json.dump(my_obj, filename)
