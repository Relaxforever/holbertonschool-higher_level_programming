#!/usr/bin/python3
def print_last_digit(number):
    percent = 0
    if number > 0:
        percent = number % 10
    if number < 0:
        percent = number % -10

    if percent < 0:
        percent = percent * -1
        print("{}".format(percent), end="")
    else:
        print("{}".format(percent), end="")
    return(percent)
