#!/usr/bin/python3
if __name__ == "__main__":
    for s in dir('hidden_4'):
        if s[:2] != '__':
            print(s)
