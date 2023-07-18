"""
Assignment;
-Using a while loop, write two functions that can output even numbers and odd numbers 
in the range of 100 with the increments of tens.
"""

def print_even_numbers():
    num1 = 0
    while num1 <= 100:
        if num1 % 2 == 0:
            print(num1)
        num1 += 10

print_even_numbers()

def print_odd_numbers():
    num2 =1 
    while num2 <= 100:
        if num2 % 2 != 0:
            print(num2)
        num2 += 10

print_odd_numbers()













