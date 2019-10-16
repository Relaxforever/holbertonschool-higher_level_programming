#!/usr/bin/python3
from json import load
"""
    Creates a JSON object from a file ,kill me
"""


def load_from_json_file(filename):
    with open(filename, encoding='utf-8') as file_js:
        return load(file_js)
