#!/usr/bin/python3
"""
    module that writes to a file
"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as file_r:
        return file_r.write(text)
