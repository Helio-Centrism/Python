# Write a program to print the elements of a list i a single line.(list is the parameter of the function)
cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"]
heroes = ["Ironman", "Captain America", "Thor", "Hulk", "Black Widow", "Hawkeye"]

print(heroes[0], heroes[1], heroes[2], heroes[3], heroes[4], heroes[5])

def ele_single(list): # here list is the parameter of the function
    for item in list: # here it means that for each element in the list
        print(item, end = " ") # here it means that print the element and end with a space

ele_single(cities)