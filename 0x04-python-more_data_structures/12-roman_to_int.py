#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False:
        return None
    elif roman_string is None:
        return None
    answer = 0
    dictRoman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    comp = [dictRoman[i] for i in roman_string]
    for a in range(len(comp)):
        answer += comp[a]
        if comp[a - 1] < comp[a] and a != 0:
            answer -= (comp[a - 1] + comp[a - 1])
    return answer
