#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if len(value) != 2 or (value[0] < 0 or value[1]) < 0 or not isinstance(value, tuple) or \
        not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size is 0:
            print()
        else:
            for row in range(self.__size):
                print(" " * self.__position[0], end='')
                for column in range(self.__size):
                    print("#", end="")
                print()
