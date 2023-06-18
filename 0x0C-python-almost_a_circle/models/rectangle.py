#!/usr/bin/python3
"""This is a class called Rectangler that inheits from the class
called Base"""


from models.base import Base


class Rectangle(Base):
    """This represents a class called Rectangle
    with its own attributes and the getters and
    setters for its attribute"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The class constructor of theclass Rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Property getter for instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter fdore the attribute: width"""
        self.__width = value

    @property
    def height(self):
        """Property getter for instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets the height for attribute height"""
        self.__height = value

    @property
    def x(self):
        """property getter for attribute 'x' """
        return self.__x

    @x.setter
    def x(self, value):
        """this sets the method for the attributre called 'x' """
        self.__x = value

    @property
    def y(self):
        """property getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """This sets the method forthe y attribute"""
        self.__y = value
