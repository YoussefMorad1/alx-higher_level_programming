#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(number, end=" is ")
if number == 0:
    print("zero")
elif number > 0:
    print("positive")
else:
    print("negative")
