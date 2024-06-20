# Constructor in Python
# basically it is like a __init__ function i.e, it is used to initialize the object of the class.
# It is called when an object of the class is created.
# so Constructor is defined as the function which is automatically called when an object of the class is created.
# All classes have a function called __init__(), which is always executed when the object is being initiated.

""" How init function works in Python """
class Student:
    
    def __init__(self, name, marks):  # init function is used to initialize the object of the class. it is called when an object of the class is created. it is defined as the function which is automatically called when an object of the class is created.
        self.name = name # self is used to access the attributes and methods of the class. name is the attribute of the class Student.
        self.marks = marks
        print("adding new student in our database") # it will print the object of the class Student.
        

s1 = Student("karan", 98)  # creating an object of the class Student where s1 is the object of the class Student. Student() is the constructor of the class Student. it will call the init function of the class Student. Where karana is the argument passed to the init function.
print(s1.name, s1.marks)  # it will print the object of the class Student.

s2 = Student("Arjun", 76) 
print(s2.name, s2.marks)  # it will print the object of the class Student.



