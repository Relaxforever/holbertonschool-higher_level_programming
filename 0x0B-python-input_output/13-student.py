#!/usr/bin/python3
""" This module has a student Class """


class Student:
    """ A student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves the dict """
        if attrs is None:
            return self.__dict__
        else:
            dict_2 = dict()
            for key in attrs:
                if key in self.__dict__.keys():
                    dict_2[key] = self.__dict__[key]
            return dict_2

    def reload_from_json(self, json):
        """ reloads json """
        if json == {}:
            pass
        else:
            self.first_name = json["first_name"]
            self.last_name = json["last_name"]
            self.age = json["age"]
