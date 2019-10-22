#!/usr/bin/python3

from models.rectangle import Rectangle
""" Module from Square class """


class Square(Rectangle):
    """ This class is a square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ the initialization file """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string representation of the class """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}/{} - {}]".format(
            class_name,
            self.id, self.x,
            self.y, self.width)

    @property
    def size(self):
        """ getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value
