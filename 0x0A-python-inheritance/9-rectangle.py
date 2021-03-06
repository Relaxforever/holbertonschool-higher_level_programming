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


class Rectangle(BaseGeometry):
    """ a class that inherits from base"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ implements the area function """
        return self.__width * self.__height

    def __str__(self):
        objnam = self.__class__.__name__
        return '[{}] {}/{}'.format(objnam, self.__width, self.__height)
