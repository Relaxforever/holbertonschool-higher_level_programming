#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for x in a_dictionary:
        if x == key:
            a_dictionary.pop(key)
            break
    return a_dictionary
