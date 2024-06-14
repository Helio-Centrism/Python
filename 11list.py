# List in Python
# A list is a collection of items that are ordered and changeable. In Python, lists are created by placing the items inside square brackets [] separated by commas.
# A list is a built in datatype  that stores the set of values.
# It can store elements of different datatypes.(int, float, string, etc)
# marks = [10, 20, 30, 40, 50]

marks = [94.4, 89, 454.0, 34, .32]
print(marks)
print(type(marks))
# A list can have any number of items, and they may be of different types (integer, float, string, etc.). A list can also have another list as an item. This is called a nested list.

print(marks[0])
print(len(marks))

student = ["John", 87, "dehradun"]
print(student)

# List are mutauable i.e. we can change the values of the list.
# List can be changed by using the index number of the element.

student[1] = 90
print(student)

#slicing the list is similar to slicing the string.

print(student[0:2])