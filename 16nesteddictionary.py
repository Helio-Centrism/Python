# Methods in Dictionary 

# 1. dict.keys() method 
# The keys() method returns a view object that displays a list of all the keys in the dictionary.
# Syntax: dict.keys()
dict = {
    "name": "Naruto",
    "Subjects": {
        "Physics": 90,
        "Maths": 78,
        "Chemistry": 89,
        }
}
print(dict.keys())
print(list(dict.keys())) # converting the view object to list
print(len(list(dict.keys()))) # getting the length of the list

# 2. dict.values() method
# The values() method returns a view object that displays a list of all the values in the dictionary.
# Syntax: dict.values()
print(dict.values())
print(list(dict.values())) # converting the view object to list
print(len(list(dict.values()))) # getting the length of the list

# 3. dict.items() method
# The items() method returns a view object that displays a list of dictionary's key-value tuple pairs.
# Syntax: dict.items()
print(dict.items())

# 4. dict.get() method
# The get() method returns the value of the specified key.
# Syntax: dict.get(key)
print(dict ["name"]) 
print(dict.get("name")) 
#here we may get error if the key is not present in the dictionary but in get() method we will get None
# beacuse it does not throw an error if the key is not present in the dictionary. 


# 5. dict.update() method
# The update() method updates the dictionary with the specified key-value pairs.
# Syntax: dict.update({key: value})

dict.update({"name": "Naruto Uzumaki"})
print(dict)

new_dict = {"age": 23, "is_adult": True, "name": "tsunade"}
dict.update(new_dict)
print(dict)
