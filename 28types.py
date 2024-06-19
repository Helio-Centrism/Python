# Types of Functions in Python
# 1. Built-in functions: Functions that are built into Python.
# Example: print(), input(), len(), range(), type(), etc. 
print("Hello World")
print("hello vishal") # end = "\n" by default
#this is a built in function in python.
# 2. User-defined functions: Functions defined by the user.
# these are the functions that are defined by the user.


# Default Parameters
# Default parameters are the parameters that are set to a default value if no argument value is passed during the function call.
# Example:
'''
def calc_pro(a,b):
    print(a*b)
    return
calc_pro() # TypeError: calc_pro() missing 2 required positional arguments: 'a' and 'b' because we have not passed any arguments to the function calc_pro.
'''
# To avoid this error we can set the default values to the parameters.
# Example:
def calc_pro(a=10, b=20):
    print(a*b)
    return
calc_pro()  