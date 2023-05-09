#!/usr/bin/python3
change = -33
letter = ord('z')
if letter == 'b':
    change = 30
while letter >= ord('A'):
    x = chr(letter)
    print("{}".format(x), end="")
    letter += change

    if change == -33:
        change = 31
    else:
        change = -33
