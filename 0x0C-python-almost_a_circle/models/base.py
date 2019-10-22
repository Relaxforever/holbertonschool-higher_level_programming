#!/usr/bin/python3
""" base module """
from json import dumps


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return dumps([])
        else:
            return dumps(list_dictionaries)
