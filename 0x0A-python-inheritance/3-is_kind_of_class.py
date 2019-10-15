#!/usr/bin/python3
""" This module checks if the class is the same instance
"""


def is_kind_of_class(obj, a_class):
    """ this checks the kind of class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
