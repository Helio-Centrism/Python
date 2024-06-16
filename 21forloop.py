# For Loop in Python
# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.
# Loops are used for sequential traversal.For traversing list, string, tuples etc.

# Syntax:
# for element in sequence: # sequence can be list, tuple, string, etc.
#     # code block / some work

list = [1, 76, 3, 467, 55, 64, 74, 83, 9, 10]

for el in list:
    print(el)

# Example:
veggies = ["potato", "tomato", "onion", "carrot", "cucumber", "beetroot", "radish", "spinach", "cabbage", "cauliflower"]
for val in veggies:
    print(val)

# Example:

str = "ich liebe Python"

for char in str:
    print(char)
else:
    print("Loop ended")
