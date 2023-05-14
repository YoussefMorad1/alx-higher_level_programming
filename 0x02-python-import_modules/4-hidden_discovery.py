#!/usr/bin/python3
if __name__ == "__main__":
    import ast
    for s in ast.parse('hidden_4'):
        if s[:2] != '__':
            print(s)
