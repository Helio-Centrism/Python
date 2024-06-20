# Class & Instance Attributes
# Attributes are the properties of the object. Attributes are defined in the class and are accessed using the object of the class. it can have any data type.
# There are two types of attributes in Python:

# 1. Class Attributes: Attributes that are defined in the class are called class attributes. They are shared by all the objects of the class. They are defined outside the constructor.
# 2. Instance Attributes: Attributes that are defined inside the constructor are called instance attributes. They are unique to each object of the class.

# Example:

class Student:
    college_name = "ABC College"  # class attribute
    name = "anonymous"  

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("karan", 98)
s2 = Student("Arjun", 76)

print(s1.name, s1.marks)  # it will print the object of the class Student.
# SO if we have instance attributes with the same name then they will not be shared by the objects of the class. They are unique to each object of the class.
# so we use it with self keyword to make it unique to each object of the class.
# Example:
#IN THE ABOVE EXAMPLE WE HAVE INSTANCE ATTRIBUTES NAME AND MARKS WHICH ARE UNIQUE TO EACH OBJECT OF THE CLASS STUDENT.
# SO IF WE HAVE INSTANCE ATTRIBUTES WITH THE SAME NAME THEN THEY WILL NOT BE SHARED BY THE OBJECTS OF THE CLASS. THEY ARE UNIQUE TO EACH OBJECT OF THE CLASS.
print(s2.college_name)  # it will print the class attribute of the class Student.
print(Student.college_name)  # it will print the class attribute of the class Student.
