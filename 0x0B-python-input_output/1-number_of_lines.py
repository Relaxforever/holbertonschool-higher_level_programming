#!/usr/bin/python3
"""
    this module reads the number of lines of a textfile.
"""


def number_of_lines(filename=""):
    with open(filename, encoding='utf-8') as file_r:
        lines = file_r.readlines()
        return len(lines)
