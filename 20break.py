# Break and Continue in Python

# Break in Python
# The break statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.
#is used to terminate the loop when encountered.
# Syntax:
# break
# Example:
# print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1 

# Continue in Python
# The continue statement is used to skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration.   
# Syntax:
# continue

# Example:
# print numbers from 1 to 10 but skip 5
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1