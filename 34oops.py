# OOP in Python
# Object-oriented programming (OOP) is a programming paradigm that is based on the concept of objects, which can contain data in the form of fields (often known as attributes), and code, in the form of procedures (often known as methods).
# to map with real world scenarios, we started using objects in code.
# why we use OOP?
# 1. It provides a clear modular structure for programs which makes it good for defining abstract data types in which implementation details are hidden.
# 2. Objects can also be reused within an across applications. The reuse of software also lowers the cost of development.
# 3. It makes software easier to maintain. Since the design is modular, part of the system can be updated in case of issues without a need to make large-scale changes.
# how did we start our learning?
# 1. we started our learning with procedural programming where we used functions to write the code.
# 2. we used functions to write the code.
# 3. Object oriented programming is a way of programming where we use classes and objects.

""" 
Class: A class is a blueprint for the objects. It defines a data type that contains data and code.
Object: An object is an instance of a class. When a class is defined, no memory is allocated but when it is instantiated (i.e. an object is created) memory is allocated.

"""

# Class
# Class is a blueprint for creating objects. A class defines the attributes and methods that an object can have.

""" Creating class in Python """

# Syntax of creating a class
class Student:  # class definition where student is the name of the class.
    name = "karan"  # attribute of the class

# Creating an object of the class(instance of the class)
# we need to create an object of the class to access the attributes and methods of the class.

s1 = Student()  # creating an object of the class Student where s1 is the object of the class Student. Student() is the constructor of the class Student.
print(s1.name)  # accessing the attribute of the class Student using the object s1.

s2 = Student()  # creating another object of the class Student
print(s2.name)  # accessing the attribute of the class Student using the object s2.



class Car:
    color = "red"
    brand = "BMW"
    model = "X5"
    year = 2020

c1 = Car()
print(c1.color)
print(c1.brand)
print(c1.model)