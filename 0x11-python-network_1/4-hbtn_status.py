#!/usr/bin/python3
from requests import get
if __name__ == "__main__":
    response = get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
