#!/usr/bin/python3
from requests import get
from sys import argv
if __name__ == "__main__":
    response = get(argv[1])
    dict = response.headers
    if dict['X-Request-Id']:
        print(dict['X-Request-Id'])
