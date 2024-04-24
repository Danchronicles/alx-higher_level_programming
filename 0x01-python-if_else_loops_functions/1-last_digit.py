#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_number = abs(number)
last_digit = abs_number % 10
print("The last digit of")
print(number)
print("the sting is")
print(last_digit, end=" ")
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("the string is and is 0")
else:
    print("and is less than 6 and not zero")