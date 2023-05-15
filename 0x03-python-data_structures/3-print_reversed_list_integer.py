#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    lst = my_list[:]
    lst.reverse()
    for x in lst:
        print('{:d}'.format(x))
