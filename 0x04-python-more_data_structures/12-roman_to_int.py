#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or if type(roman_string) is str:
        return 0
    value = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    revert = roman_string[::-1]
    for invict in range(len(revert)):
        if invict != 0 and roman[revert[invict - 1]] > roman[revert[invict]]:
            value = value - roman[revert[invict]]
        else:
            value = value + roman[revert[invict]]
    return value
