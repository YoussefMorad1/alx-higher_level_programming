#!/usr/bin/python3
""" module of read file """
def read_file(filename=""):
    """ read file funcion """
    with open(filename, encoding='UTF-8') as f:
        print(f.read(), end='')
