#!/usr/bin/python3
""" This module has a student Class """


class Student:
    """ A student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves the dict """
        return self.__dict__
