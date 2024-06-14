# Write a program to check if a list contains a plaindrome or not. hint (use copy() method)

list1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list3 = list1.copy()
list4 = list2.copy()
list3.reverse()
list4.reverse()

if(list1 == list3):
    print("List1 is a palindrome")
else:
    print("List1 is not a palindrome")

if(list2 == list4):
    print("List1 is a palindrome")
else:
    print("List2 is not a palindrome")
