# del keyword in Python
# del is used to delete the reference to an object. It does not delete the object from memory. It is used to delete the reference to an object.
# used to delete object properties or object itself.
# Syntax:
# del object_name
# del object_name.property_name
# Example:

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("karan", 98)
print(s1.name)  # it will print the object of the class Student.

del s1 # it will delete the name attribute of the object s1. 
print(s1.name)  # it will give an error because we have deleted the name attribute of the object s1.


# Output: karan
# Explanation: In the above code we have created a class named Student. In the class Student we have created a constructor that takes two arguments name and marks. Then we have created an object of the class Student and printed the name attribute of the object s1. Then we have deleted the object s1. Then we have tried to print the name attribute of the object s1. But it will give an error because we have deleted the object s1. So it will give an error.


#*********************************************************************************************************************************************************************


# Private(like) attributes and methods in Python

# Private attributes and methods in Python

class Account:
    def __init__(self, acc_no, acc_password):
        self.acc_no = acc_no
        self.acc_password = acc_password
        

acc1 = Account(123456, 1234)

print(acc1.acc_no)  # it will print the acc_no attribute of the object acc1.
print(acc1.acc_password)  # it will print the acc_password attribute of the object acc1.

# But 