#!/usr/bin/python3
""" pytho module of course """
import json
import sys


def do_work():
    """ important function of course """
    lst = []
    try:
        with open('add_item.json', 'r', encoding='UTF-8') as f:
            lst = json.load(f)
    except Exception:
        pass
    for i in range(1, len(sys.argv)):
        lst.append(sys.argv[i])
    with open('add_item.json', 'w', encoding='UTF-8') as f:
        json.dump(lst, f)


if __name__ == '__main__':
    do_work()
