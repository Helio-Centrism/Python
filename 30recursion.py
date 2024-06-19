# Recursion in Python
# Recursion is the process of defining something in terms of itself. A function that calls itself is called a recursive function.
# A recursive function is a function that calls itself during its execution.
# When a function call itself then it is called recursion.

# print n to 1 backwords
"""
def print_n(n):
    if n == 0:   # base case means the condition where the function will stop calling itself.
        return
    print(n)
    print_n(n-1)
""" 

# we can do all the task which uses loops using recursion but recursion is not always the best way to do the task.

def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)
    
show(5) # now if we want to to print the numbers from 5 to 1 then we can use recursion to do this task.
show(6)