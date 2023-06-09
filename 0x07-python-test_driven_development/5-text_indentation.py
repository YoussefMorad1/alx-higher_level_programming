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
    for ch in text:
        if ch != ' ':
            s += ch
        elif len(s) >= 1 and s[len(s) - 1] != '\n':
            s += ch
        if ch in ('.', '?', ':'):
            s += '\n\n'
    print(s)
