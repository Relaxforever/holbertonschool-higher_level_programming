#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    for i in range(len(argv)):
        if (len(argv) - 1) == 0:
            print("{} arguments.".format((len(argv) - 1)))
        elif i == 0 and (len(argv) - 1) <= 1:
            print("{} argument:".format((len(argv) - 1)))
        elif i == 0:
            print("{} arguments:".format((len(argv) - 1)))
        elif i != 0:
            print("{}: {}".format(i, argv[i]))
