#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy_list = my_list.copy()
    for i in range(len(copy_list)):
        if copy_list[i] == search:
            copy_list[i] = replace
    return copy_list
