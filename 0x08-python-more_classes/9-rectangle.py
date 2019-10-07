#!/usr/bin/python3
"""
    This Module contains the rectangle Class it will be
    expanded upon the more we write in it
    Made by FFCC
"""


class Rectangle:
    """ This class we will make a classic Rectangle,it will be
    expanded upon the more we write in it """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This method is called when a new object is created """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """ notifies when someone deletes an instance
            DAD ON THEM DELETERS"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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
                        rectangle += str(self.print_symbol) +\
                            str(self.print_symbol)
                        hashtag += 2
            else:
                for i in range(self.__width):
                    rectangle += str(self.print_symbol)
                    hashtag += 1
        return rectangle

    def __repr__(self):
        """ Sets the repr of the rectangle """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def bigger_or_equal(rect_1, rect_2):
        """ compares the Area of the rectangle and kills me """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(height=size, width=size)
