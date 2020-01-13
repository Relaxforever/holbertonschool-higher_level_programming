#!/usr/bin/python3
from requests import get, post
from sys import argv
if __name__ == "__main__":
    try:
        if len(argv) == 2:
            param = {'q': argv[1]}
        else:
            param = {'q': ''}
        response = post("http://0.0.0.0:5000/search_user", param)
        response = response.json()
        print("[{}] {}".format(response['id'], response['name']))
    except KeyError:
        print("")
    except Exception:
