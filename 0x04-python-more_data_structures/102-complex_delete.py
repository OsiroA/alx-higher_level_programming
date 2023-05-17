def complex_delete(a_dictionary, value):
    newDict = []
    for key in a_dictionary.keys():
        if a_dictionary[key] == value:
            newDict.append(key)
    for key in newDict:
        del a_dictionary[key]
    return a_dictionary
