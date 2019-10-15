#!/usr/bin/python3
"""
This module contains a class Mylist that
sorts everything
"""


class MyList(list):

    def print_sorted(self):
        list_sort = self[:]
        list_sort.sort()
        print(list_sort)
