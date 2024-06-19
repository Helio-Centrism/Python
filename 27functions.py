# Functions in Python
# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
# is  a block of statements that performs a specific task.
# it is a reusable code.

#for Example: if we have given a task to add two numbers then we can write a function to add two numbers and we can call that function whenever we want to add two numbers.
"""
# a = 5
# b = 10
# sum = a + b
# print(sum)

# #more lines of code

# a = 15
# b = 10
# sum = a + b
# print(sum)

# # more lines of code
# a = 5
# b = 110
# sum = a + b
# print(sum)

# #So we see taht in order to do sum of two numbers we have to write the same code again and again. So to avoid this we can write a function to add two numbers and we can call that function whenever we want to add two numbers.

# #Syntax of function:
# ''' #def function_name(parameters): Function definition
#     #Some work
#     #return value 
# '''
# def cal_sum(a , b): # function definition it takes two parameters a and b it can take any number of parameters.
#     sum = a + b
#     print(sum)
#     return sum # return statement is used to return the value from the function. here it returns the sum of two numbers. 

# cal_sum(5, 10) # function call it calls the function cal_sum and passes the values 5 and 10 to the function which are stored in a and b respectively.here the values are called arguments.
# cal_sum(15, 10) # function call 
# cal_sum(5, 110) # function call 
"""

def calc_sum(a, b):  # function definition it takes two parameters a and b it can take any number of parameters.
    return a + b

sum = calc_sum(2323, 234555)  # Function call it calls the function cal_sum and passes the values 2323 and 234555 to the function which are stored in a and b respectively.here the values  are called arguments.
print(sum) 

def print_hello():
    print("Hello")

print_hello()  # function call
print_hello()  # function call

print(print_hello())  # function call

