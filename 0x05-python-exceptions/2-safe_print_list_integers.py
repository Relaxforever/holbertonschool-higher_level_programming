#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    a = 0
    while (y < x):
        try:
            print("{:d}".format(my_list[y]), end="")
        except ValueError:
            a += 1
            pass
        except TypeError:
            a += 1
            pass
        finally:
            y = y + 1
    if y > 0:
        y = y - a
    print()
    return y
