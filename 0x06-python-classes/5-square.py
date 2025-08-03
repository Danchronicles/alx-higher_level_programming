#!/usr/bin/python3

"""Defines a classs square"""

class Square:
    """Represents a square"""
    
    def __init__(self, size=0):
        """Initiliazes a new square instance
        
        Args:
            size(int): The size of the square(default is 0)
        """
        self.size = size
    
    @property
    def size(self):
        """Retrives the private attribute __size"""
        return self.__size
    
    @size.setter
    def size (self, value):
        """sets the value of the size with validation
        
        Args:
            value (int): The new size of the square
            
        Raises: 
            TypeError if value is not an interger
            ValueError if value < 0
        """
        if not isinstance(value, int):
            raise TypeError ("size must be an interger")
        if value < 0:
            raise ValueError ("size must be >= 0")
        self.__size = value
    def area(self):
        """Calculates and returns the current area of the square"""
        return self.__size * self.__size
    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
            
            