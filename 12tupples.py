# Tupples in Python
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# A tuple is a built in datatype  that lets us create immutable sequence of values.
# It can store elements of different datatypes.(int, float, string, etc)
# list vs tuple vs strings 
# list is mutable i.e. we can change the values of the list.
# Tuple is immutable i.e. we cannot change the values of the tuple.
# Strings are immutable i.e. we cannot change the values of the string.
# Syntax: tuple = (value1, value2, value3, ...) we use round brackets to create a tuple.

# Example:
tuple = (1, 2, 3, 4, 5)
print(type(tuple))
print(tuple[3])
# tuple[3] = 10 # this will give an error because tuple is immutable.

tup = ()
print(type(tup))
print(tup)
tub = (1) # this is not a tuple
print(type(tub))
print(tub)]
tub = (1,) # this is a tuple
print(type(tub))