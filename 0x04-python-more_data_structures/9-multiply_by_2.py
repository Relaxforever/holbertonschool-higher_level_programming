#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy_dict = a_dictionary.copy()
    for x in copy_dict:
        copy_dict[x] = copy_dict[x] * 2
    return copy_dict
