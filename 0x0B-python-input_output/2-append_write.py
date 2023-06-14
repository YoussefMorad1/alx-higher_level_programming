#!/usr/bin/python3
""" module of append file """


def append_file(filename="", text=""):
    """ append to file funcion """
    with open(filename, 'a', encoding='UTF-8') as f:
        return f.write(text)
