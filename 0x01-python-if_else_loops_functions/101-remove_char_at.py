#!/usr/bin/python3
def remove_char_at(str, n):
    killer = ""
    for cont in range(len(str)):
        if cont != n:
            killer = killer + str[cont]
    return killer
