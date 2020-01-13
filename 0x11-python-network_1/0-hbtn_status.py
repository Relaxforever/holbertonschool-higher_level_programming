#!/usr/bin/python3
# Python script that fetches url and shows the body information of it.
from urllib import request
with request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))
