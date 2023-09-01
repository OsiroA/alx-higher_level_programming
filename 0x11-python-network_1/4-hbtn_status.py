#!/usr/bin/python3
"""
this fetches a particular site
"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    # with urllib.request.urlopen(url) as response:
    content = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(content.text)))
    print("\t- content: {}".format(content.text))
