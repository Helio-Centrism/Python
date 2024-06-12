
# Variables in Python :" A variable is a name that refers to a value or which is given to the memory location in a program"
# examples of variables : name = "vaibhav" , age = 22

name = "vaibhav" # it is a strings
age = 22
cgpa = 8.5
print("my name is ", name)
print("my age is ", age)
print("my cgpa is ", cgpa)

# Rules for variable names in python
# 1. A variable name must start with a letter or the underscore character
# 2. A variable name cannot start with a number
# 3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# 4. Variable names are case-sensitive (name, Name and NAME are three different variables)
# 5. Variable names should be descriptive and meaningful (name, age, cgpa are better names than n, a, c)
# 6. Avoid using reserved words (keywords) as variable names (if, else, for, while, etc.)
# 7. Avoid using special characters in variable names (except underscore) (name@, name!, name$, etc. are not allowed)
# 8. Use underscores to separate words in a variable name (first_name, last_name, age_of_student, etc.)
# 9. Use camel case or snake case for multi-word variable names (firstName, lastName, ageOfStudent, etc.)


print(type(name))
print(type(age))

# data types in python
# 1. Numbers : int, float, complex
# 2. Strings : str
# 3. Boolean : bool
# 4. List : list
# 5. Tuple : tuple
# 6. Set : set
# 7. Dictionary : dict
# 8. none

age = 22
old = False
a = None
print(type(age))
print(type(old))
print(type(a))