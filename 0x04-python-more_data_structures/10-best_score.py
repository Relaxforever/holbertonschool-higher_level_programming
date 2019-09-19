#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = ""
    biggest2 = 0
    if not a_dictionary:
        return None
    for x in a_dictionary:
        if a_dictionary[x] > biggest2:
            biggest = x
            biggest2 = a_dictionary[x]
    return biggest
