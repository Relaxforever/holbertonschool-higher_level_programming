#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        cont = 0
        for j in i:
            if len(i) - 1 > cont:
                print("{:d} ".format(j), end="")
            else:
                print("{:d}".format(j), end="")
            cont = cont + 1
        print()
