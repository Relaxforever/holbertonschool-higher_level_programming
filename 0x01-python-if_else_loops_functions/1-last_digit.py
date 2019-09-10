#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lastone = number % 10
else:
    lastone = number % -10
if lastone > 5:
    print("Last digit of {} is {}\
 and is greater than 5".format(number, lastone))
elif lastone < 6 and lastone != 0:
    print("Last digit of {} is {}\
 and is less than 6 and not 0".format(number, lastone))
elif lastone == 0:
    print("Last digit of {} is {} and is 0".format(number, lastone))
