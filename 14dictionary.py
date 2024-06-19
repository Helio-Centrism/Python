# Dictionary in Python
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
# Dictionaries are used to store data values in key:value pairs.
# They are unordered mutable(changeable) and dont allow dublicate keys.

dict = {
    "name": "John",
    "percentage": 87,
    "marks": [45, 67, 89, 90],
    # where name, percentage, marks are keys and John, 87, [45, 67, 89, 90] are values.
    "age": 34,
    "is_adult": True,
    "topics": ("python", "java", "c++"),

}
print(dict)
print(type(dict))

# Properties of Dictionary
# 1. Unordered: Dictionaries are unordered. The order in which the items are added is not fixed.
# 2. Changeable: We can change the values of the dictionary.
# 3. Indexed: We can access the items of the dictionary by using the key.
# 4. No Duplicate keys: Dictionaries do not allow duplicate keys. If we use the same key twice, the second occurrence will overwrite the first.

# Accessing the items of the dictionary
# We can access the items of the dictionary by using the key.
print(dict["name"])
print(dict["percentage"])
print(dict["marks"])
print(dict["age"])
print(dict["is_adult"]) 

dict["name"] = "John Doe" # changing the value of the key name
print(dict)

dict["name"] = 23 # overwriting the value of the key name it does not create a new key.
print(dict)

null_dict = {} # we can create empty dictionary or null dictionary
null_dict["name"] = "naruto" # we can add the key value pair in the dictionary later.
print(null_dict) 

