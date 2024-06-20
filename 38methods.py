# Methods in python
# Methods are functions that are defined inside the class. They are used to define the behavior of an object.
# Methods are called using the object of the class. They can have any number of arguments.
# Methods are functions that belongs to the object.
# in our class we can store two things i.e, attributes and methods.

# Example:
# creating a class named Student

class Student:
    def __init__(self, name, marks):  # init function is used to initialize the object of the class. it is called when an object of the class is created. it is defined as the function which is automatically called when an object of the class is created.
        self.name = name # self is used to access the attributes and methods of the class. name is the attribute of the class Student.
        self.marks = marks
            
    def welcome(self):
        print("Welcome student", self.name)  # it will print the object of the class Student.

    def get_marks(self):
        return self.marks

s1 = Student("karan", 97)
s1.welcome()  # it will print the object of the class Student.
print(s1.get_marks())  # it will print the object of the class Student.