#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square("hola")
print("")
try:
    print_square("hola")
except Exception as e:
    print(e)
print("")
