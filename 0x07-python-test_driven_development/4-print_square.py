#!/usr/bin/python3
def print_square(size):
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    for number in range(size):
        print("#" * size)
