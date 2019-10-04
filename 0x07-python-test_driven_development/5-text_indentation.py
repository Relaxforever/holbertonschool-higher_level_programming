#!/usr/bin/python3
"""
 Doing what needs to be done in this module, this function will
 indent a text so when it detects a special character wil print a
 newline like . ? or :
"""


def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_t = text.replace(".", ".\n\n")
    new_t = new_t.replace(":", ":\n\n")
    new_t = new_t.replace("?", "?\n\n")

    print("\n".join([line.strip() for line in new_t.split("\n")]), end="")
