#!/usr/bin/python3
from json import dump
"""
    A function that passes from JSON to string.
"""


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding='utf-8') as file_w:
        return dump(my_obj, file_w)
