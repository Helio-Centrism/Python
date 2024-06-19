# Write a function to find the factorial of n (n is a parameter)

n = int(input("Enter the number: "))

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

print(factorial(n))