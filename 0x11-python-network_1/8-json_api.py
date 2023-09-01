#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request
to a link given with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
        url = 'http://0.0.0.0:5000/search_user'
        parameter = {'q': letter}
        response = requests.post(url, data=parameter)
        try:
            JSONResponse = response.json()
            if JSONResponse:
                userID = JSONResponse.get('id')
                userName = JSONResponse.get('name')
                print("[{}] {}".format(userID, userName))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
