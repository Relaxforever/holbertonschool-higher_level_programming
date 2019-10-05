#!/usr/bin/python3
""" a module that prints a square"""


def print_square(size):
    """ prints a square depending of the size given """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for number in range(size):
        print("#" * size)
