#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    # Divides element by element two lists and returns a new list with the results
    #it will iterate through list_length times. In each iteration, it will attempt to divide corresponding elements from My_list_1 and My_list_2. It must handle IndexError - if the list are too short, ZerodivisionError - if division by zero occurs, Typeerror/Valuerror - if elements are not numbers.
    
    new_results_list = []
    
    for i in range(list_length):
        #initiliaze the current result for the current division to 0.0
        #This will be the default value if any error occurs
        
        current_division_result = 0.0
        
        try:
            #1, Access elements from both lists i.e "My_list[1] & my_list[2]"
            #if "i" is out of bounds an index error will occur
            
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            
            current_division_result = num1 / num2
            
        except IndexError:
            # This handles cases where "i" is greater than or equal to the length of my_list_1 or my_list_2.
            
            print("out of range")
            
        except ZeroDivisionError:
            # This handles the cases where the denominator (num2) is 0.
            
            print("division by 0")
            
        except (TypeError, ValueError):
            # This handles cases where one or both elements are not intergers or floats
            
            print("Wrong type")
            
        finally:
            # This block is always executed  before the try statements completes, regardless of wherther an exception was raised or handled.
            
            pass
        # Append the result of the current division (either the calculated  value or 0.0 if an error occured to the list of results) 
        new_results_list.append(current_division_result)
            