#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a square"""
    
    def __init__(self, size = 0):
        """Initializes a new square instance
        
        Args: 
        size (int): The size of the square defaults into zero (default to 0)
        """
        
        self.size = size
        
    @property
    def size(self):
            """Retrieves the private instance attribute'_size' """
            return self.__size
        
    @size.setter
    def size(self, value):
        """Sets the size of the square with validation
        
        Args:
        value(int):The new size for the square
        
        Raises:
        TypeError: If a value is not an integer
        ValueError: if a value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("size be an interger")
        if value < 0 :
            raise TypeError("size must be > 0")
            self.__size = value
            
    def area (self):
        """calculates and returns the current area of the square"""
        return self.__size * self. __size
        