#!/usr/bin/python3
"""
This script takes in a URL, sends a request to it
and diplays the value of a specified variable found in
the header of the response
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    # send an HTTP GET request to the URL using with
    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
        # print(x-Request-Id)
