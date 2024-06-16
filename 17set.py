# Sets in Python
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
# each element in the set is unique i.e. it does not allow duplicate values and is immutable.
# A set is a built in datatype  that stores the set of values.
# It can store elements of different datatypes.(int, float, string, etc)
# Syntax: set = {value1, value2, value3, ...} we use curly brackets to create a set.

# Example:
num = {1, 2, 3, 4, 5, 2 ,2,2, 3, 4, "hello", "world", 5.5, 6.6} # set does not allow duplicate values. 
print(type(num))
print(num)
print(len(num)) # length of the set


null_set = set() # we can create empty set or null set
print(type(null_set))

