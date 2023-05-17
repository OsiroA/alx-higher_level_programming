#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) < 1:
        return 0
    sUm = 0
    wEight = 0
    for column in my_list:
        sUm += column[0] * column[1]
        wEight += column[1]
    return (sUm / wEight)
