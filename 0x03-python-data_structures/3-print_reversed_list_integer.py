#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lst = my_list[:]
    lst.reverse()
    for x in lst:
        print('{:d}'.format(x))
