# Create a new file "practice.txt" using python. Add the following data in it : 
"""  Hi everyone
    we are learning File I/O 
    using Java.
    I Like programming in Java."""

with open("practice.txt", "w") as f:
    f.write("Hi everyone \nwe are learning File I/O\nusing Java.\nI Like programming in Java.")


# write a function which replaces all the Java words with Python in the file "practice.txt"
""" so first we need to read the data from the file then we need to replace the Java words with Python that is we will overwrite then we need to write the data to the file. """

with open("practice.txt", "r+") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)


# Search if the word learning is present in the file "practice.txt" or not.
word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1): # find() function is used to find the word in the string.
        print("The word", word, "is present in the file.") 
    else:   
        print("The word", word, "is not present in the file.")
    
