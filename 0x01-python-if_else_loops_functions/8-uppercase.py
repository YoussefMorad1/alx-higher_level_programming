#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97:
            print('{}'.format(ord(c) - 97 + ord('A')))
        else:
            print('{}'.format(c), end='')
