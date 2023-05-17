#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for k, v in a_dictionary.items():
        if key in a_dictionary.keys() and value in a_dictionary.values():
            a_dictionary[key] = value
        elif key in a_dictionary.keys() and value not in a_dictionary.values():
            a_dictionary[key] = value
        else:
            a_dictionary[key] = value
        return (a_dictionary)
