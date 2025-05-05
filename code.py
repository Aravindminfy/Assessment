# This is the python file
# The main aim is to learn about basic git command 
# Write a code to print the factorial number
# Use function and add logic to the function 

def factorial(n): 
    if n == 1 or n == 0: # base condition
        return 1
    else:
        return n * factorial(n-1) # logic for factorial of an number
    
number = 5
result = factorial(number)
print(f"Factorial of the number {number} is {result}") # answer to the end user 