#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= ord('z'):
            print('{}'.format(ord(c) - 97 + ord('A')), end='')
        else:
            print('{}'.format(c), end='')
