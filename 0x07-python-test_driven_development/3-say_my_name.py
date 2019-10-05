#!/usr/bin/python3
""" Module that prints a string with Hi my name is {} """


def say_my_name(first_name, last_name=""):
    """A function that get's the first name and last name of a person
    and prints it in the standard output
    The function will check if both instances given are strings
    in case of not TypeError will be presented """
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
