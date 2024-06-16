# Search for a number x in this tuple using loop:
num = [1,4,9,16,25,36,49,64,81,100]
i = 0
x = int(input("Enter the number to search: "))
while i < len(num):
    if x == num[i]:
        print("Number found at index: ", i)
        break
    i += 1