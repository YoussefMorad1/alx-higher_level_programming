#!/usr/bin/python3
def st_division(my_list_1, my_list_2, list_length):
    ls = []
    for i in range(list_length):
        c = 0
        try:
            c = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print('division by 0')
        except IndexError:
            print('out of range')
        except Exception:
            print('wrong type')
        finally:
            ls[i] = c
    return ls
