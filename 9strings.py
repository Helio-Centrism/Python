# Strings in Python 

# A string is a sequence of characters enclosed within a pair of single or double quotes. In Python, strings are immutable, which means they cannot be changed after they are created. However, you can assign a new value to the same variable name. Strings are ordered sequences of characters, and each character in the string has an index number associated with it. The index number starts from 0, and it can go up to n-1, where n is the length of the string.
# So basically it is a datatye which stores the sequence of characters.


str1 = 'hello'
str2 = "hello2"
str3 = '''hello3'''
str4 = """hello4"""
print(str1)
print(str2)
print(str3)
print(str4) 

# So when writing a string if we need to give it a next line then we use escape sequence characters.
# Escape sequences are the sequence of characters that doesn't represent itself when used inside a string literal, but it is interpreted in a special way.
# Escape sequences start with a backslash (\) character. For example, \n represents a new line, \t represents a tab, etc.
# Here are some of the escape sequences in Python.
# Escape Sequence	Meaning
# \\	Backslash (\)   
# \'	Single quote (')
# \"	Double quote (")
# \n	New line
# \t	Tab
# \b	Backspace
# \r	Carriage return
# \f	Form feed
# \ooo	Octal value

# Example

a = "hello may i know how shall i help u in developing the code"
print(a)
# if we want to print the string in the new line then we use \n
b = "hello \n may i know how shall i help u in developing the code"
print(b)

# basic operations on strings are:
# 1. Concatenation
# 2. Repetition
# 3. Slicing
# 4. Membership
# 5. Length
# 6. Iteration
# 7. Comparison
# 8. String formatting
# 9. Escape sequences
# 10. Raw strings
# 11. Conversion between strings and other data types

# 1. Concatenation
# Concatenation is the process of combining two strings. In Python, you can concatenate two strings using the + operator.

# Example 1: Concatenation of two strings
a = "hello"
b = "sir"
print(a + b)

# Example 2: Length of the string
a = "hello"
b = "sir"
print(len(a))
print(len(b))
print(len(a + b))

# 2. Repetition
# Repetition is the process of repeating a string multiple times. In Python, you can repeat a string using the * operator.

# Example: Repetition of a string
a = "hello"
print(a * 3)

# 3. Slicing
# Slicing is the process of extracting a substring from a string. In Python, you can slice a string using the [] operator.
# The syntax for slicing a string is string[start:end:step]. Here, start is the starting index of the substring, end is the ending index of the substring, and step is the step size for slicing.

# Example 1: Slicing a string
a = "hello"
print(a[1:4])
print(a[1:4:2]) # here 2 is the step size which means it will skip the 2nd character
print(a[-1:]) # here -1 means the last character of the string
