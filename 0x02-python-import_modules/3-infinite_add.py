#!/usr/bin/python
if __name__ == "__main__":
    cont = 0
    from sys import argv
    for i in range(len(argv)):
        if argv[i] != argv[0]:
            cont += int(argv[i])
    print("{}".format(cont))
