# Type Conversion in Python 
#  Type conversion refers to the conversion of one data type into another data type.
#  In Python, we can convert one type of data into another type using the following in-built functions.
#  1. int() : This function converts any data type to integer.
#  2. float() : This function is used to convert any data type to a float.
#  3. ord() : This function is used to convert a character to an integer.
#  4. hex() : This function is to convert integer to hexadecimal string.
#  5. oct() : This function is to convert integer to octal string.
#  6. tuple() : This function is used to convert to a tuple.
#  7. set() : This function returns the type after converting to set.
#  8. list() : This function is used to convert any data type to a list type.
#  9. dict() : This function is used to convert a tuple of order (key,value) into a dictionary.
#  10. str() : This function is used to convert the integer into a string.
#  11. complex(real,imag) : This function converts real numbers to complex(real,imag) number.
#  12. chr() : This function converts integer to its corresponding ASCII character.
#  13. bool() : This function is used to convert a value to a Boolean value.

#it automatically converts the data type of the variable to the data type of the value assigned to it.

# Example 1: Converting integer to float
a = 5
b = 5.5
c = 5.0
print("Data type of a:", type(a))
print("Data type of b:", type(b))
print("Data type of c:", type(c))
d = a + b + c
print("Data type of d:", type(d))


# type casting : it is a process of converting one data type to another data type manually.
# Example 1: Converting integer to float
a = 5
print("Data type of a:", type(a))

b = float(a)
print("Data type of b:", type(b))

# Example 2: Converting float to integer
a = 5.6
print("Data type of a:", type(a))

b = int(a)
print("Data type of b:", type(b))

# Example 3: Converting string to integer
a = "10"
print("Data type of a:", type(a))

b = int(a)
print("Data type of b:", type(b))

# Example 4: Converting integer to string
a = 10
print("Data type of a:", type(a))

b = str(a)
print("Data type of b:", type(b))

# Example 5: Converting string to float
a = "10.5"
print("Data type of a:", type(a))

b = float(a)
print("Data type of b:", type(b))

# Example 6: Converting float to string
a = 10.5
print("Data type of a:", type(a))

b = str(a)
print("Data type of b:", type(b))
