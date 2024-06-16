# nested Dictionary in Python
# A dictionary can contain another dictionary, which in turn can contain dictionaries themselves, and so on to create a nested dictionary.
# syntax : dict = {key1: {key2: {key3: value3}}}

# Example:

dict = {
    "name": "Naruto",
    "Subjects": {
        "Physics": 90,
        "Maths": 78,
        "Chemistry": 89,
        }
}
# where name, Subjects are keys and Naruto, {Physics: 90, Maths: 78, Chemistry: 89} are values.
# where Physics, Maths, Chemistry are keys and 90, 78, 89 are values.
print(dict)
print(dict["Subjects"]) # accessing the value of the key Subjects
print(dict["Subjects"]["Physics"]) # accessing the value of the key Physics