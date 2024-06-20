# Private(like) attributes and methods in Python

# Private attributes and methods in Python
"""
class Account:
    def __init__(self, acc_no, acc_password):
        self.acc_no = acc_no
        self.acc_password = acc_password
        

acc1 = Account(123456, 1234)

print(acc1.acc_no)  # it will print the acc_no attribute of the object acc1.
print(acc1.acc_password)  # it will print the acc_password attribute of the object acc1.
"""
# so this is a bad practice beacuse we are exposing the attributes of the class to the outside world. So to avoid this we can use the private attributes and methods in Python. 
# To make the attributes and methods private we can use the double underscore __ before the attribute and method name.

class Account:
    def __init__(self, acc_no, acc_password):
        self.acc_no = acc_no
        self.__acc_password = acc_password

    def reset_pass(self):
        print(self)
        

acc1 = Account(123456, 1234)
print(acc1.acc_no)  # it will print the acc_no attribute of the object acc1.
# print(acc1.__acc_password)  # it will give an error because we have made the acc_password attribute private. So we can not access the private attribute outside the class.

print(acc1._Account__acc_password)  # it will print the acc_password attribute of the object acc1. Because we can access the private attribute using the class name.


# Conceptual Implementations in Python
# Private attributes and methods are meant to be used only within the class and are not accessible from outside the class.

# Lets create another class

class Person:
    __name = "Vaibhav"

    def __hello(self):
        print("Hello person!")

    def welcome(self):
        self.__hello()

p1 = Person()
#print(p1.__name)  # it will give an error because we have made the name attribute private. So we can not access the private attribute outside the class.

# print(p1.__hello())  # it will give an error because we have made the hello method private. So we can not access the private method outside the class.

print(p1.welcome()) 