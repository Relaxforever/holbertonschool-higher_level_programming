#!/urs/bin/python3
def no_c(my_string):
    strkiller = ""
    for i in my_string:
        if i is not 'C' and i is not 'c':
            strkiller += i
    return strkiller
