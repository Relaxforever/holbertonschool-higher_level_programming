#!/usr/bin/python3
""" This module checks if the class is the same instance
"""


def inherits_from(obj, a_class):
    """ this class checks if someone inherits from
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
