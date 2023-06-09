#!/usr/bin/python3
"""
text indentation module
"""


def text_indentation(text):
    """
    main text indentation function
    """
    if type(text) != str:
        raise TypeError('text must be a string')
    s = ''
    lst = '\n'
    for ch in text:
        if lst != '\n' or ch != ' ':
            s += ch
            lst = ch
            if ch in ('.', '?', ':'):
                s += '\n\n'
                lst = '\n'
    print(s)
