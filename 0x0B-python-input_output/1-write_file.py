#!/usr/bin/python3
""" module of write file """


def write_file(filename="", text=""):
    """ read file funcion """
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(text)
