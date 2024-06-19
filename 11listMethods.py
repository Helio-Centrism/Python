# Methods for Lists in Python

list = [1, 76, 3, 467, 55, 64, 74, 83, 9, 10]
# 1. append() method
# The append() method adds an element to the end of the list.
# Syntax: list.append(element)
print(list.append(11)) # None is returned because the element is added to the list in place and the return value is None.
print(list)

# 2. sort() method
# The sort() method sorts the elements of a list in ascending order.

# Syntax: list.sort()
print(list.sort()) # None is returned because the list is sorted in place and the return value is None.
print(list)

# 3. sort(reverse = True) method
# The sort(reverse = True) method sorts the elements of a list in descending order.
# Syntax: list.sort(reverse = True)
print(list.sort(reverse = True)) # None is returned because the list is sorted in place and the return value is None.
print(list)

# sorting is possiblle in strings too

# 4. reverse() method
# the reverse() method reverse the list. 

list.reverse()
print(list)

# 5.insert() method 
# the insert() method insert the element at index
# syntax : list.insert(idx, ele)

list.insert(4, 555555)
print(list)

# 6. remove() method
# The remove() method removes the first occurence of the element

list.remove(555555)
print(list)

# 7. pop() method
# the pop() method is used to remove the element at any index

list.pop(6)
print(list) 

