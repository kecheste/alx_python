""" Module that contains class Rectangle,
inheritance of class Base
"""
from models.base import base


class Rectangle(base.Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes instances """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
