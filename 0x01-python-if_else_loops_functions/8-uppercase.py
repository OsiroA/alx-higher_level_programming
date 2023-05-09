#!/usr/bin/python3
def uppercase(str):
    result = ""
    for letter in str:
        if 'a' <= letter <= 'z':
            upper = chr(ord(letter) - ord('a') + ord('A'))
            result += upper
        elif letter == "\n" or letter == "\r":
            result += letter
        else:
            result += letter
    print("{}".format(result))
