#!/usr/bin/python3
from requests import get, post
from sys import argv
if __name__ == "__main__":
    response = get(argv[1])
    if response.status_code >= "400":
        print(response.status_code)
    else:
        print(response.text)