#!/usr/bin/python3

def print_square(size):
    """
    prints a square with the character # of a given size
    Args:
        size(int): size length of the square
        
    Raise:
        TypeError: if size is not an interger(int) or if its a float
        ValueError: If size is a negative interger
    """
    
    # validate 'size' type (i.e must be an interger)
       # It checks that size is not a string, list, or other object
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an interger")
    
    # Explicitly handle float inputs (Rule : size must be an interger,) and if size is a float and is less than 0, raise a TypeError. floats fails requarement of being an interger
    if isinstance(size, float):
        raise TypeError("size must be an interger")
    
    # Validates 'size' value
    #this handles the case where 'size' is a negative integer
    if size < 0:
        raise ValueError("size must be > 0")
    
    # Print the square
    #if size is 0, the loops run zero times, printing nothing(correct behavior)
    for _ in range(size):
        print("#" * size)
    

        
     