#!/usr/bin/python3
def magic_calculation(a, b, c):
    if c == '<':
        if a < b:
            return True
        else:
            return False
    if c == '>':
        if a > b:
            return True
        else:
            return False
    if c == '+':
        return a + b
    if c == '*':
        return a * b
    if c == '-':
        return a - b