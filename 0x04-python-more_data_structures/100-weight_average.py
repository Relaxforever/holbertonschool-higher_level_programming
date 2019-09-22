#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    sum = 0
    add = 0
    for value1, value2 in my_list:
        sum += value1 * value2
        add += value2
    return sum / add
