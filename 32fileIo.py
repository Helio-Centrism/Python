# File I/O in Python
# python can be used to perform operations on a file.(read, write, append, delete data from a file)
# I/O means input and output.

"""Types of all Files
1. Text File: A file that contains text data. e.g. .txt, .c, .cpp, .py, .html, .css, .js, .java,.docs, .log, etc.
2. Binary File: A file that contains binary data. e.g. .jpg, .png, .mp3, .mp4, .pdf, .exe, .zip, .rar, etc.
"""

# Basic Operations on a File that can be performed
""" *****************Open, read & close File**********************"""
# Opening a file
# we have to open a file before reading and writing data to it.
# f = open("file_name", "mode")

# Modes of opening a file
# 1. "r": Opens a file for reading. (default mode)
# 2. "w": Opens a file for writing. It will create a new file if it does not exist or truncate the file if it exists. i.e it will overwrite the file.
# 3. "x": Creates a new file. If the file already exists, the operation will fail.
# 4. "a": Opens a file for appending at the end of the file without truncating it. It will create a new file if it does not exist.
# 5. "t": Opens a file in text mode. (default mode)
# 6. "b": Opens a file in binary mode.
# 7. "+": Opens a file for updating (reading and writing) i.e r+w, r+a, w+r, w+a, a+r, a+w, x+r, x+w, x+a

# if we dont mention the mode then by default the file is opened in read mode.

# Reading a file
f = open("demo.txt", "r")
# data = f.read()  # read() function is used to read the data from the file.
# data = f.read(5)  # read(n) function is used to read the n characters from the file.
data = f.readline()
data = f.readline()  # readline() function is used to read a single line from the file.
print(data)
print(type(data))
f.close()  # close() function is used to close the file.

# data = f.read()   reads entire file
# data = f.readline() reads a single line from the file


# Writing to a file
# 1. Overwriting the file
f = open("demo.txt", "w")
f.write("Ni hao!!!")# overwrites the entire file.
f.close()

# 2. Appending to a file
f = open("demo.txt", "a")
f.write("Ni hao!!! I would like to become an AI enginer")# appends the data to the file.
f.write("\narigato") # \n is used to move the cursor to the next line.
f.close()

g = open("sample.txt", "w")
g.close()  # creates an empty file. it simply creates a file with the name sample.txt and closes it.simillary we can create a file with the name sample.txt by using the mode "a".

# 3. Reading and Writing to a file
f = open("demo.txt", "r+")
f.write("abc")  # it will overwrite the first 3 characters of the file.
print(f.read())  # it will read the remaining data of the file.
f.close() # it will not truncate the file and write the data to the file.

# 4. Appending and Reading to a file
f = open("demo.txt", "a+")
f.write("abc")  # it will append the data to the file.
f.seek(0)  # it will move the cursor to the beginning of the file.
print(f.read())  # it will read the data of the file.
f.close() # it will not truncate the file and write the data to the file.

# 5. Writing and Reading to a file
f = open("demo.txt", "w+")
f.write("abc")  # it will overwrite the entire file.
f.seek(0)  # it will move the cursor to the beginning of the file.
print(f.read())  # it will read the data of the file.
f.close()  # it will truncate the file and write the data to the file.


# with syntax
# with syntax is used to open a file and close it automatically.
# with open("file_name", "mode") as f:
#     f.write("Hello World")
#     f.read()
#     f.readline()
#     f.write("Hello World")

with open("demo.txt", "r") as f: # where f is the file object.
    data = f.read()
    print(data)
    print(type(data))  # <class 'str'>  it means that the data is of string type.

with open("demo.txt", "w") as f:
    f.write("Ni hao!!!")


# Deleting a file 
# using the os module we can delete a file.
# Module(like a code library) is a file written by another programmer that generally has a functions which we can use in our code.

import os
os.remove("sample.txt")  # it will delete the file sample.txt
