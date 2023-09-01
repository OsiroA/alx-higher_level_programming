#!/bin/usr/python3
"""
This script lists 10 commits in a given repositoryu by a given user
"""
import requests
import sys.argv


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    request = requests.get(url)
    commits = request.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
