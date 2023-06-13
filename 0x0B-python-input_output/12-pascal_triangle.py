#!/usr/bin/python3
"""task 12"""


def pascal_triangle(n):
    """this function returns a list kf lists of integrrs representing the triangle"""
    list1 = []
    if n <= 0:
        return list1
    for numb in range(0, n):
        if numb == 0:
            list1.append([1])
        else:
            list2 = []
            len_last = len(list1[-1])
            index = len(list1) - 1
            for numb2 in range(0, len_last):
                if numb2 == 0:
                    list2.append(1)
                if numb2 == len_last - 1:
                    list2.append(1)
                else:
                    list2.append(list1[idx][numb2] + list1[idx][numb2 + 1])
            list1.append(list2)
    return list1
