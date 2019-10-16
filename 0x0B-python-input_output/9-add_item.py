#!/usr/bin/python3
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
"""
    a module that adds arguments to a python list, and then saves
them to a file
"""

try:
    list_argv = load_from_json_file("add_item.json")
    """with open("add_item.json", 'a', encoding='utf-8') as file_w:"""
except FileNotFoundError:
    list_argv = []

finally:
    for cont in range(1, len(argv)):
        list_argv.append(argv[cont])
    save_to_json_file(list_argv, "add_item.json")
