#!/usr/bin/python3


"""Module to set an attribute"""
def add_attribute(object, attr, value):
    """
    Whenever it can it will try to add an attribute.
    """
    if hasattr(object, "__dict__"):
        object.__setattr__(attr, value)
    else:
        raise TypeError("can't add new attribute")
