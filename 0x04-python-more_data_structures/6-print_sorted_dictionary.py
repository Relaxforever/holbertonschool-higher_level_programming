#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for keys in sorted(a_dictionary):
        print("{}: ".format(keys), end="")
        print("{}".format(a_dictionary[keys]))
