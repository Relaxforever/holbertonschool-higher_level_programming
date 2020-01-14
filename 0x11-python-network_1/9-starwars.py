#!/usr/bin/python3
# get the info of star wars characters
from requests import get, post
from sys import argv
if __name__ == "__main__":
    response = get("https://swapi.co/api/people/?search={}".format(argv[1]))
    star_dict = response.json()
    print("Number of results: {}".format(star_dict['count']))
    results_list = star_dict['results']
    for character_dict in results_list:
        print(character_dict.get('name'))
