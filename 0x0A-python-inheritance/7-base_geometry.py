#!/usr/bin/python3
""" this module contains geometry Class """


class BaseGeometry:
    """this class contains the basic geometry """
    def area(self):
        """ this class raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the value variable """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
