#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end='\n')
        return True
    except ValueError:
        print("Exception: {}".format(Error), file=sys.stderr)
        return False
    except TypeError:
        print("Exception: {}".format(Error), file=sys.stderr)
        return False
