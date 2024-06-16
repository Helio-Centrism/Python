# Search for a number x in this tuple using a loop:

tup = (1,4,9,16,25,36,49,64,81,100) # Tuple
x = int(input("Enter the number to search: "))
for el in tup:
    if el == x:
        print("Number found at index: ", tup.index(el))
        break