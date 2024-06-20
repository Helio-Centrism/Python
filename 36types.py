# Types of Constructor in Python:
# 1. Default Constructor: Constructor with no arguments. if we donot make any constructor then python will create a default constructor for us.
# 2. Parameterized Constructor: Constructor with arguments. if we make a constructor with arguments then it is called parameterized constructor.
# Example:
class Student:
    
    # Default Constructor
    def __init__(self):
        pass

    # Parameterized Constructor
    def __init__(self, name, marks):  # init function is used to initialize the object of the class. it is called when an object of the class is created. it is defined as the function which is automatically called when an object of the class is created.
        self.name = name # self is used to access the attributes and methods of the class. name is the attribute of the class Student.
        self.marks = marks
        print("adding new student in our database") # it will print the object of the class Student.
        

s1 = Student("karan", 98)  # creating an object of the class Student where s1 is the object of the class Student. Student() is the constructor of the class Student. it will call the init function of the class Student. Where karana is the argument passed to the init function.
print(s1.name, s1.marks)  # it will print the object of the class Student.

s2 = Student("Arjun", 76) 
print(s2.name, s2.marks)  # it will print the object of the class Student.
