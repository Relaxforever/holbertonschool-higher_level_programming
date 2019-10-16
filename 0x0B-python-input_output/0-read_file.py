#!/usr/bin/python3
"""
    This module has a function that reads file
"""


def read_file(filename=""):
    """ This function reads files """
    with open(filename, encoding='utf-8') as read_file:
        print(read_file.read(), end="")
