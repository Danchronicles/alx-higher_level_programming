#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    # my_list - The list to print first elements and only intergers from
    # x - number of elements to access in MY_list
    
    count = 0 #  It loops through the X elements i.e its a variable to store
    
    for i in range(x):# iterates through the x elements and assign coresponding indexs to i
        try:
            print("{:d}".format(my_list[i]), end = "")
        except (ValueError, TypeError):
            pass
        except IndexError: # handles the case where the X is larger than the my_list length
            break
            # Exists when the number of indexes has reached its limits.we are at the end of list
        else:
            count += 1
    print("")
    return count
            