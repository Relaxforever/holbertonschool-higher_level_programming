#!/usr/bin/python3
def uniq_add(my_list=[]):
    cont = 0
    for i in set(my_list):
        cont += i
    return cont
