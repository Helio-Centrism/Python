# Methods in Set

# 1. add() method
# The add() method adds an element to the set.
# Set is Mutable but the elements in the set are immutable
# Syntax: set.add(element)

set = {1, 2, 3, 4, 5}
set.add(6)
set.add((1, 2, 3, 4, 5)) # tuple is immutable 
print(set)

# 2. remove() method
# The remove() method removes the specified element from the set.
# If the element is not present in the set, a KeyError is raised.
# Syntax: set.remove(element)

set.remove(6)
print(set)
# set.add([1, 2, 3, 4, 5]) # TypeError: unhashable type: 'list'beacuse list is mutable
# print(set)

# 3. clear() method
# The clear() method removes all the elements from the set.
# Syntax: set.clear()

set.clear()
print(set)

# 4. pop() method
# The pop() method removes a random element from the set.
# Syntax: set.pop()

set = {1, 2, 3, 4, 5}
set.pop()
print(set)

# 5. union() method
# The union() method returns a new set with all items from both sets.
# Syntax: set.union(set)

set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
set3 = set1.union(set2)
print(set3)

# 6. intersection() method
# The intersection() method returns a new set with all items that are present in both sets.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.intersection(set2)
print(set3)

# 7. difference() method
# The difference() method returns a new set with all items that are present in set1 but not in set2.
# Syntax: set1.difference(set2)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.difference(set2)
print(set3)

# 8. symmetric_difference() method
# The symmetric_difference() method returns a new set with all items that are present in exactly one of the sets.
# Syntax: set1.symmetric_difference(set2)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.symmetric_difference(set2)
print(set3)




