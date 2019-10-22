#!/usr/bin/python3
""" Rectangle class """

from models.base import Base


class Rectangle(Base):
    """ class to build rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ the getter of the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height setter """
        return self.__height

    @height.setter
    def height(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x getter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ this methods gets the area of the rectangle """
        return self.height * self.width

    def display(self):
        """ this functions print the Rectangle with # """
        rectangle = ""
        if self.__width is 0 or self.__height is 0:
            print(rectangle)
        else:
            for y_mov in range(self.y):
                print()
            for cont in range(self.height):
                if self.x is not 0:
                    print(" " * self.x, end="")
                print("#" * self.width)

    def __str__(self):
        """ prints the str reprensetation """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}/{} - {}/{}".format(
            class_name,
            self.id, self.x,
            self.y, self.width,
            self.height)

    def update(self, *args, **kwargs):
        """ updates arguments """
        if len(args) > 0 and args is not None:
            att = ["id", "width", "height", "x", "y"]
            cont = 0
            for attri in args:
                setattr(self, att[cont], args[cont])
                cont = cont + 1
        if len(kwargs) > 0 and kwargs is not None:
            for ky, vle in kwargs.items():
                setattr(self, ky, vle)
