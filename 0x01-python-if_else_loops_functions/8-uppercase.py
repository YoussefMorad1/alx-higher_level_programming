#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print('{:c}'.format(max(ord(c) - ord('a'), 0) + ord('A')), end='')
    print()
