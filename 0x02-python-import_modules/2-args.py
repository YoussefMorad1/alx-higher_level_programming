#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ln = len(argv) - 1
    print('{} argumen{}{}'.format(ln, 't' if ln == 1 else 'ts',
          '.' if ln == 0 else ':'))
    for i in range(1, ln + 1):
        print('{}: {}'.format(i, argv[i]))
