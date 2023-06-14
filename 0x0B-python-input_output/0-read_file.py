#!/usr/bin/python3
""" module of read file """
def read_file(filename=""):
    """ read file funcion """
    with open(filename) as f:
        print(f.read())
