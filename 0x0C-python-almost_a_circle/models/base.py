#!/usr/bin/python3
"""this is for the base file"""


class Base:
    """The class tcalled Base with various attributes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is a class constructor"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
