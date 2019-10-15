#!/usr/bin/python3
""" This module checks if the class is the same size
"""


def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True
    else:
        return False
