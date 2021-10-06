#!/usr/bin/python3
"""class named square"""


class Square:
    """square class"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise ValueError("size must be an integer")

    def area(self):
        return(self.__size ** 2)
