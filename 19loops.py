# Loops in Python
# Loops are used to repeat instructions multiple times.
# In Python, there are two types of loops:
# 1. while loop
# 2. for loop

# While Loop
# The while loop is used to iterate over a block of code as long as the test expression (condition) is true.
# Syntax:
# while condition:
#     # code block / some work

# Example:

#print hello 5 times
count = 0 # initialize the counter because we need to print hello 5 times if not then the loop will run infinitely. # Alsso know as iterator beacuse it iterates over the code block.
while count <= 5: # condition to check if the counter is less than or equal to 5
    print("Hello") # print hello
    count += 1 # increment the counter by 1 after each iteration. 

# Example:
# print numbers from 1 to 100

i = 1
while i <= 1000:
    print(i)
    i += 1
# Example:
# print even numbers from 1 to 100
num = 1
while num <= 100:
    if num % 2 == 0:
        print(num)
        num += 1 
    else:  # if the number is odd then increment the counter by 1
        num += 1 # increment the counter by 1 after each iteration.
print("Loop ended")
    
# Example:
a = 5
while a > 0:
    print(a)
    a -= 1
