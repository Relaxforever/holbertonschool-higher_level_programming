#!/usr/bin/python3
from requests import get, post
from sys import argv
if __name__ == "__main__":
    param = {'email': argv[2]}
    response = post(argv[1], param)
    print(response.text)
