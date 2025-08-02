#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        pass
        """Defines a square with a private size attribute"""
        
        """Initializes a new square instance .
        Args:
        size (int, optional): The size of the square. Defaults to 0
        Raises:
        TypeError: if size is not interger
        ValueError: If size is less than 0"""
        
        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
        
    def area(self):
        return self.__size ** 2
        
        