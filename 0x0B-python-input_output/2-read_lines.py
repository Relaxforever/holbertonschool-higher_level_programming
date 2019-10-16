#!/usr/bin/python3
"""
   this module has a function that reads n lines
"""


def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as file_r:
        lines = file_r.readlines()
        if nb_lines > 0 and nb_lines <= len(lines):
            for cont in range(nb_lines):
                print(lines[cont], end="")
        else:
            for cont in range(len(lines)):
                print(lines[cont], end="")
