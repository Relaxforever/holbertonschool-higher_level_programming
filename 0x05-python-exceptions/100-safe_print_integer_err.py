#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end='\n')
    except ValueError as Error:
        print("Exception: {}".format(Error), file=sys.stderr)
        return False
    except TypeError as Error:
        print("Exception: {}".format(Error), file=sys.stderr)
        return False
    else:
        return True
