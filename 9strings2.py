# String Functions in Python
# In Python, strings are objects of the str class. The str class comes with a number of string functions that allow you to manipulate strings.

# Some of the commonly used string functions in Python are:

str = "i am a coder"
str.endswith("er.") #  Returns True if the string ends with the specified suffix, otherwise returns False.
str.startswith("i") # Returns True if the string starts with the specified prefix, otherwise returns False.
str.capitalize() # Converts the first character of the string to uppercase.
print(str)
print(str.endswith("er."))
print(str.startswith("i"))
print(str.capitalize())

str.replace("coder", "developer") # Replaces all occurrences of the specified substring with another substring.
str.replace("a" , "was") # Replaces all occurrences of the specified substring with another substring.
print(str.replace("coder", "developer"))
print(str.replace("a" , "was"))


print(str.find("o"))   # Searches the string for a specified value and returns the position of where it was found.
print(str.find("a"))   # Searches the string for a specified value and returns the position of where it was found.

print(str.count("a"))  # Returns the number of times a specified value occurs in a string.
