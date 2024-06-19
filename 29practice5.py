# Write a function to input a number and return the string odd if the number is odd and even if the number is even.


def odd_eve(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter the number: "))

print(odd_eve(n))