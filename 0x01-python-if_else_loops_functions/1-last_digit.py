#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
m = abs(number) % 10
if number < 0:
    m *= -1
print(f'Last digit of {number} is {m} and is ', end="")
if m > 5:
    print('greater than 5')
elif m == 0:
    print(0)
else:
    print('less than 6 and not 0')
