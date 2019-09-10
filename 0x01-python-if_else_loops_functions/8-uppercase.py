#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        rest = ord(str[i])
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            rest = rest - 32
        print("{}".format(chr(rest)), end="")
    print()
