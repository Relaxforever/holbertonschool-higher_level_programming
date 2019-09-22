#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not value:
        return None
    for x in list(a_dictionary):
        if a_dictionary[x] is value:
            a_dictionary.pop(value)
            break
    return a_dictionary
