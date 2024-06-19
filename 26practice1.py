# write a program to find the sum of first n numbers using a  while loop.

n = int(input("Enter the number: "))

sum = 0
i = 1
while i <= n: # here it means that the loop will run until i is less than or equal to n.
    sum += i  # here it means that sum = sum + i
    i += 1    # here it means that i = i + 1
print("The sum of first", n, "numbers is: ", sum)
