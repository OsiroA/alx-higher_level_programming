#!/usr/bin/python3
"""task 6"""


import json


def load_from_json_file(filename):
    """This function creates an object from a JSON file"""
    with open(filename, encoding="utf-8") as afile:
        return json.load(afile)
