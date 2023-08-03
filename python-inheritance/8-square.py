"""Implements a Square based on Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Args:
        size - size of square
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)


__doc__ = """
this is documentation for my module
"""
