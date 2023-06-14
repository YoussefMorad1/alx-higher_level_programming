#!/usr/bin/python3
""" module of append file """


def append_write(filename="", text=""):
    """ append to file function """
    with open(filename, 'a', encoding='UTF-8') as f:
        return f.write(text)
