#!/usr/bin/python3

def safe_print_list(my_list = [], x = 0):
    
# print x elements of a list using try/except
# my_list - the list to print elements from
# X - The number of elements to attempt to print
    count = 0
    for i in range(x):
        try:
            #attempt to accesss the element at index i
            #Accessing an index that is out of bounds for the list will cause an exception during execution[1]. specifically this will raise an index error
            print(my_list[i], end = "")
            count += 1
        except IndexError:
            # This handles exceptions that occur during executions of the try clause
            # We specifically catch the indexError because it is the exception raised when trying to access a list index that does not exist 
            # once an indexError is caught, it means we've gone beyond the list's actual length. we stop processing further elements
            break
    print("")
    return count
