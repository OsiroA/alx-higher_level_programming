#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    PAT = sys.argv[2]
    url = 'https://api.github.com/users/{}'.format(username)
    req = requests.get(url, auth=requests.auth.HTTPBasicAuth(username, PAT))
    print(req.json().get('id'))
