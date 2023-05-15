#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    l = my_list[:]
    l.reverse()
    for x in l:
        print('{:d}'.format(x))
