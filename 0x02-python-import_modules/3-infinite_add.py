#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    cont = 0
    for i in range(len(argv)):
        if argv[i] != argv[0]:
            cont += int(argv[i])
    print("{}".format(cont))
