#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ct = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ct += 1
        except ValueError:
            continue
        except Exception:
            print()
            return ct
    print()
    return ct

print(safe_print_list_integers([1, 2, 'hi', 3, 4], 7))
