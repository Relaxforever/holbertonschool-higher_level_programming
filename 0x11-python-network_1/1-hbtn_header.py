#!/usr/bin/python3
# takes in a URL sends request to the URL and displays the X-Request-Id
from urllib import request
from sys import argv
with request.urlopen(argv[1]) as response:
    header_dict = response.headers
    print(header_dict.get('X-Request-Id'))
