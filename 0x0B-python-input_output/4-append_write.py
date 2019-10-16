#!/usr/bin/python3
""" appends a file at the end of the string """


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as file_a:
        return file_a.write(text)
