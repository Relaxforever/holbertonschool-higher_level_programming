#!/usr/bin/python3
# this script finds a peak in a list of integers


def find_peak(list_of_integers):
    sizeofl = len(list_of_integers)
    if len(list_of_integers) == 0:
        return None
    first = 0
    last = sizeofl - 1
    while first < last:
        center = (first + last) // 2
        if list_of_integers[center] > list_of_integers[center + 1]:
            last = center
        else:
            first = center + 1
    return list_of_integers[first]
