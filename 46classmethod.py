"""
class method in python

"""
# class method is used to access the class attributes and class methods.

# A class method is bound to the class and receives the class as the implicit first argument.

# Note: - static method can't access or modify class state and generally for utility which means that they are not bound to the class and can't access or modify class state.

class Person:
    name = "Vaibhav"

    def change_name(self, new_name):
        """self.new_name = new_name # it will create a new attribute new_name of the object p1."""
        #Person.new_name = new_name # it will change the name attribute of the class Person.
        self.__class__.new_name = "Naruto" # it will change the name attribute of the class Person.

p1 = Person()
"""
p1.change_name("Karan")
print(p1.new_name)  # it will print the new_name attribute of the object p1.
print(Person.new_name)  # it will print the name attribute of the class Person."""
# so basially its trying to change the name attribute of the class Person but it is not changing the name attribute of the class Person because we are not using the class method to change the class attribute. 
# In simpler words, we are not able to change the vaibhav to karan because we are not using the class method to change the class attribute.
"""
p1.change_name("Karan")
print(p1.new_name)  # it will print the name attribute of the class Person.
print(Person.new_name)  # it will print the name attribute of the class Person.
"""
# so now we are able to change the name attribute of the class Person because we are using the class method to change the class attribute.
# In simpler words, we are able to change the vaibhav to karan because we are using the class method to change the class attribute. as by using Person.new_name = new_name we are able to change the name attribute of the class Person for all the objects of the class Person.

p1.change_name("Narutooo")
print(p1.new_name)  # it will print the name attribute of the class Person.
print(Person.new_name)  # it will print the name attribute of the class Person.


#So to use class method we have to use the @classmethod decorator.
# Example:
"""
class Student:
    @classmethod #decorator
    def college(cls):
        pass
        
"""
# Lets create a class method in the class Person.
class Person:
    name = "Vaibhaav"

    @classmethod
    def change_name(cls, new_name):
        cls.new_name = new_name # it will change the name attribute of the class Person.

p2 = Person()
p2.change_name("Monkey D Luffy")
print(p2.new_name)  # it will print the name attribute of the class Person.
print(Person.new_name)  # it will print the name attribute of the class Person.


# Output: Monkey D Luffy
#         Monkey D Luffy

# Explanation: In the above code we have created a class named Person. In the class Person we have created a class method named change_name that takes two arguments cls and new_name. Then we have created an object of the class Person and called the class method change_name using the object of the class Person. Then we have printed the new_name attribute of the object p2. It will print the name attribute of the class Person. Then we have printed the name attribute of the class Person. It will print the name attribute of the class Person. So the output of the above code will be Monkey D Luffy and Monkey D Luffy. 

"""
So we have learn three types of methods in python:
1. Instance Method(self)
we used this when we want to access the instance attributes of the class.
2. Static Method (@staticmethod)
we used this when we want to access the class attributes of the class.
3. Class Method (@classmethod)
we used this when we want to access the class attributes of the class and we want to change the class attributes of the class.
"""

#*********************************************************************************************************************************************************************

# Property Decorators in Python
# Property decorators are used to access the class attributes and class methods.
# we use @property decorator on any method in class to use the method as a property.

# Example:
"""
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percent = str((self.phy + self.chem + self.math)/3) + "%"

    def calPercentage(self):
        self.percent = str((self.phy + self.chem + self.math)/3) + "%"


s1 = Student(98, 97, 96)
print(s1.percent)  # it will print the percentage of the student.

s1.phy = 99
print(s1.phy)
#print(s1.percent)  # it will print the percentage of the student.
# So the problem is that when we change the marks of the student then the percentage of the student is not changing because we have calculated the percentage of the student in the constructor of the class Student. So we have to calculate the percentage of the student when we change the marks of the student. So to solve this problem we use the property decorator. 
# Output: 97.0%
# Explanation: In the above code we have created a class named Student. In the class Student we have created a constructor that takes three arguments phy, chem, and math. Then we have created an object of the class Student and printed the percentage of the student. Then we have changed the phy attribute of the object s1. Then we have printed the phy attribute of the object s1. Then we have printed the percentage of the student. It will print the percentage of the student.
print(s1.calPercentage())  # it will print the percentage of the student. 
print(s1.percent)  # it will print the percentage of the student.
"""
#So to do the same task we shall use the property decorator in the class Student.

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percent(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

s1 = Student(98, 97, 96)
print(s1.percent)  # it will print the percentage of the student.

s1.phy = 99
print(s1.phy)
print(s1.percent)  # it will print the updated percentage of the student.



