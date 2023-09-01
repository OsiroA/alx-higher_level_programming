#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request
to the URL with the email as parameter
and displaysa the body of the response
"""
import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    # encode the email parameter
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        # read then decode the response body
        responseBody = response.read().decode('utf-8')
        print(responseBody)
        # print("Your email is: {}".format(email))
