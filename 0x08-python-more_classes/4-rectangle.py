#!/usr/bin/python3
"""
    This Module contains the rectangle Class it will be
    expanded upon the more we write in it
    Made by FFCC
"""


class Rectangle:
    """ This class we will make a classic Rectangle,it will be
    expanded upon the more we write in it """

    def __init__(self, width=0, height=0):
        """This method is called when a new object is created """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ This method the value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ This method sets the value of width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ This method sets the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ This method sets the value of height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ this methods calculates the area of a
            Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ this method calculates the perimeter of a
            Rectangle """
        if self.__width is 0 or self.__height is 0:
            self.perimeter = 0
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """ this functions print the Rectangle with # """
        rectangle = ""
        if self.__width is 0 or self.__height is 0:
            return rectangle
        for cont in range(self.__height):
            hashtag = 0
            if cont != 0:
                rectangle += '\n'
            if (self.__height * self.__width) % 2 == 0:
                for i in range(self.__width):
                    if hashtag < self.__width:
                        rectangle += '##'
                        hashtag += 2
            else:
                for i in range(self.__width):
                    rectangle += '#'
                    hashtag += 1
        return rectangle

    def __repr__(self):
        """ Sets the repr of the rectangle """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)
