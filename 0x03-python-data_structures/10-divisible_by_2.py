#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cont = 0
    my_list_copy = my_list.copy()
    for i in my_list_copy:
        if i % 2 is 0:
            my_list_copy[cont] = True
        else:
            my_list_copy[cont] = False
        cont = cont + 1
    return my_list_copy
