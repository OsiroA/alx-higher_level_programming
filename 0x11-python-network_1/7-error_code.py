#!/usr/bin/python3
"""
This script takes in a URL, sends a request to it
and display the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    status = req.status_code
    if status < 400:
        print(req.text)
    else:
        print("Error code: {}".format(status))
