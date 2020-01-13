#!/usr/bin/python3
# sends a POST request to the URL with the email,
# and displays the body of the response
from urllib import request, error
from sys import argv
if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as answer:
        print("Error code: {}".format(answer.code))
