#!/usr/bin/python3
""" python module :) """


class MyList(list):
    """ my own list class"""
    def print_sorted(self):
        """ print list sorted """
        lst = sorted(self)
        print(lst)
