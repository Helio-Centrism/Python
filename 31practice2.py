# Write a recursive function to print all elements of a list.
# hint use list and index as parameters.


def list(n, index):
    if(index == len(n)):
        return
    print(n[index])
    list(n, index+1)

fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

list(fruits, 0)
list(fruits, 4)