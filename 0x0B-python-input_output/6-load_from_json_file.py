#!/usr/bin/python3
""" small module """
import json


def load_from_json_file(filename):
    """ from json to obj function """
    with open(filename, 'r', encoding='UTF-8') as f:
        return json.load(f)
