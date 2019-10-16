#!/usr/bin/python3
""" rebel myInt """


class MyInt(int):
    """class that get's to change a rebel integer"""

    def __eq__(self, other):
        return int(self) != int(other)

    def __ne__(self, other):
        return int(self) == int(other)
