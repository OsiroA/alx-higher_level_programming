#!/usr/bin/python3
def multiple_returns(sentence):
    lEngth = len(sentence)
    if lEngth < 1:
        firstcharacter = 0
    else:
        firstcharacter = sentence[0]
    return lEngth, firstcharacter
