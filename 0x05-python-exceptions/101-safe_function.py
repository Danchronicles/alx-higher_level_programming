#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    # executes a given function within a try except block
    # fct - A pointer to the function to be executed
    # *args - Variable arguments to pass the function 'fct'.
    
    try:
        result = fct(*args) # python functions are first class objects, so they can be passed as arguments and executed directly by calling them
        return result
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None