#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lst = my_list[:]
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = True
        else:
            lst[i] = False
    return lst

