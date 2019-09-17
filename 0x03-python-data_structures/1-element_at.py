#!/usr/bin/python3
def element_at(my_list, idx):
    len_of_list = len(my_list)
    if idx > len_of_list or idx < 0:
        return None
    return my_list[idx]
