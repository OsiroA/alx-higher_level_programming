#!/usr/bin/python3
"""
This script takes in a URL, sends a request
then displays the body of the response
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    # request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
