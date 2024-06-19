# Write a program to find the factorial of n numbers using for loop

n = int(input("Enter the number: "))

fact = 1
for i in range(1, n+1): # here it means that the loop will run from 1 to n.
    fact = fact * i # here it means that fact = fact * i
print("The factorial of", n, "is: ", fact)
