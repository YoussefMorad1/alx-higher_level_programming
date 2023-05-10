#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print('{:c}'.format(ord(c) - ord('a') + ord('A') 
            if ord(c) >= ord('a') and ord(c) <= ord('z') else ord(c)), end='')
    print()
