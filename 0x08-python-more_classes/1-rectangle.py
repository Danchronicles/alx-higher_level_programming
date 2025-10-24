#!/usr/bin/python3

class Rectangle:
    """
    Defines a rectangle with private width and height attributes, controlled via properties for validation and retrieval. 
    """
    
    def __init__(self, width = 0, height = 0):
        """
        Initializes a new Rectangle instance
        
        Args:
        width(int): The width of the rectangle defaults to 0
        Height(int): The height of the rectangle defaults to 0 
        """
        
        # Assignments must go through the setters to perform validation 
        self.width = width
        self.height = height
        
        @property
        def width(self):
            """
            Retrieves the private instance attributes  __width
            """
            # Retrieve the value from the private attribute
            return self.__width
        
        @width.setter
        def width(self, value):
            """
            Sets the private instance attribute  __width with validation
            """
            if not isinstance(value, int):
                raise TypeError("width must be an interger")
            if value < 0:
                raise TypeError("width must be an interger")
            #store the value in private attribute (double underscore prefix)
            self.__width = value
            
        @property
        def height(self):
            """
            Retrieves the private instance attribute __height
            """
            # Retrieves the value from the private attribute
            
            return self.__height
        
        @height.setter
        def height(self, value):
            """
            sets the private instance attribute __height with validation
            """
            if not isinstance(value, int):
                raise TypeError("height must be an interger")
            if value < 0:
                raise ValueError(height must be >= 0)
            #store the value in the private  (double underscore prefix)
            self. __height = value
            