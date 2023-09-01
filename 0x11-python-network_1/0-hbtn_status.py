#!/usr/bin/python3
"""
this script fetches a given website using urrlib
"""


import urllib.request
if __name__ == "__main__":
    # url to fetch is:
    url = 'https://alx-intranet.hbtn.io/status'
    # then send an HTTP GET request to the URL
    response = urllib.request.urlopen(url)
    # read the HTML content
    htmlContent = response.read()
    # print the content in the specified format by school
    print("Body response:")
    print("\t- type: {}".format(type(htmlContent)))
    print("\t- content: {}".format(htmlContent))
    print("\t- utf8 content: {}".format(htmlContent.decode('utf-8')))
