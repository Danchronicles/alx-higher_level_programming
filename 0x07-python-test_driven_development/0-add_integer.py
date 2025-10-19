#!/usr/bin/python3

def add_interger(a, b=98):
    """
    Adds two intergers. Floats are cast to intergers before addition.
    a And b must be intergers or floats
    """
    
    # Check type and raise TypeError if 'a' is not an interger or float
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an interger or b must be an interger")
    
    # cast 'a' and 'b' to intergers if they are floats
    # This process ensures that the return must be an interger
    a = int(a)
    b = int(b)
    
    #return the interger addition of a and b
    return a + b
    