#!/usr/bin/python3
""" small module """
import json


def from_json_string(str):
    """ from json to obj function """
    return json.loads(str)
