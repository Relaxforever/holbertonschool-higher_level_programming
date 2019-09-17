#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len_list = len(my_list)
    if idx >= len_list or idx < 0:
        return my_list
    my_second_list = my_list.copy()
    my_second_list[idx] = element
    return my_second_list
