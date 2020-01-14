#!/usr/bin/python3
# get the info of star wars characters
from requests import get, post
from sys import argv
if __name__ == "__main__":
    github_token = get('https://api.github.com/user', auth=(argv[1], argv[2]))
    github_token = github_token.json()
    print(github_token.get('id'))
