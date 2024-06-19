# reutrns n! (n factorial)
# Compare this snippet from 26practice3.py:

def fact(n):
    if n == 1 or n == 0:
        return 1
    return fact(n-1) * n

print(fact(5))
print(fact(0))