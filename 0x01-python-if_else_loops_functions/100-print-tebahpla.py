#!/usr/bin/python3
for i in range(ord('z'), ord('a')-1, -1):
    print(f'{i - i % 2 * 32:c}', end="")
