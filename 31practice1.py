# Write a recursive function to calculate the sum of n natural numbers. 


def sum_no(n):
    if n == 0:
        return 0 
    return sum_no(n-1) + n 

print(sum_no(56))
