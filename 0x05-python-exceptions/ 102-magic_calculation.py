#!/usr/bin/python3

def magic_calculation(a, b):
    
    result = 0
    for i in range (1, 3):
        try:
           result += (a ** b) / i
        except Exception:
            return result
         