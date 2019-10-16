#!/usr/bin/python3
from json import dumps
"""
    A function that passes from JSON to string.
"""


def to_json_string(my_obj):
    return dumps(my_obj)
