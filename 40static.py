# Static Methods in python
# Static methods in python are the methods that are defined inside the class but they do not have access to the instance of the class.
# Methods that dont use the self parameter (work at class level) are called static methods.
# Static methods are defined using the @staticmethod decorator.
# Static methods can be called using the class name or the object of the class.
# Static methods are used when we dont want to use the instance of the class.

# DECORATORS: Decorators are used to modify the behavior of the function or class. it is used to add some extra functionality to the function or class.
# Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.
# Example:
class Student:
    college_name = "ABC College"  # class attribute
    name = "anonymous"  # class attribute but when we run we get the instance attribute value because instance attribute has the same name as the class attribute and instance attribute has the priority over the class attribute.

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")  # it will print the object of the class Student.
    def get_average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your average marks is: ", sum/3)


s1 = Student("karan", [98, 97, 96])
s1.get_average()
s1.hello()  

