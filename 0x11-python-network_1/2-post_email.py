#!/usr/bin/python3
# sends a POST request to the URL with the email,
# and displays the body of the response
from urllib import request, parse
from sys import argv
if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        the_page = response.read()
        the_page = the_page.decode('utf-8')
        print(the_page)
