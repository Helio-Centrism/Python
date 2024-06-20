# 3. Inheritance in python
# Inheritance is the process by which one class acquires the properties of another class. The class that is inherited is called the parent class, and the class that inherits the properties is called the child class.
# Inheritance is used to define a new class that is based on an existing class. The new class inherits the attributes and methods of the existing class.
# Inheritance allows us to define a class that inherits all the methods and attributes of another class.

# When one class(child/derived) derives the properties of another class(parent/base) then it is called inheritance.
#Example:  
"""
class Car:
    ....


class Audi(Car):
    ....

"""
# Here Audi is the child class and Car is the parent class, because  Audi class is inheriting the properties of Car class.

# Inheritance is used to define a new class that is based on an existing class. The new class inherits the attributes and methods of the existing class.

class Car:
    @staticmethod
    def start():
        print("Car has started")

    @staticmethod
    def stop():
        print("Car has stopped")
    

class Audi(Car):
    def __init__(self, name):
        self.name = name

car1 = Audi("Audi R8")
car2 = Audi("Audi A8")

print(car1.name)
print(car1.start()) # here it will not give error because Audi class is inheriting the properties of Car class.

# Output: Audi R8
#         Car has started
#         None

# Explanation: In the above code we have created a class named Car. In the class Car we have created two static methods named start and stop. Then we have created a class named Audi that inherits the properties of the class Car. In the class Audi we have created a constructor that takes one argument name. Then we have created two objects of the class Audi and printed the name attribute of the object car1. Then we have called the start method using the object car1. It will print the name attribute of the object car1 and then it will print Car has started. It will print None because the start method does not return anything. 

#*********************************************************************************************************************************************************************


# Types of Inheritance in Python
# 1. Single Inheritance
# Single inheritance is the process by which one class(child/derived) derives the properties of another class(parent/base) then it is called single inheritance.
# Above program is the example of single inheritance.
"""
# 2. Multi-level Inheritance
 Multi-level inheritance is the process by which one class(child/derived) derives the properties of another class(parent/base) and then the derived class becomes the parent class for another class(child/derived).

 """
# Example:
class Bike:
    @staticmethod
    def start():
        print("Bike has started")

    @staticmethod
    def stop():
        print("Bike has stopped")

class Kawasaki(Bike):
    def __init__(self, brand):
        self.brand = brand

class Ninja(Kawasaki):
    def __init__(self, model):
        self.model = model

bike1 = Ninja("Ninja 300")
bike2 = Ninja("Ninja 650")
bike3 = Ninja("Ninja 1000")

print(bike1.model) # it will print the model attribute of the object bike1.
print(bike1.start()) # it will print the model attribute of the object bike1 and then it will print Bike has started because Ninja class is inheriting the properties of Bike class.

# So the above code is the example of multi-level inheritance.

# Output: Ninja 300
#         Bike has started
#         None

# Explanation: In the above code we have created a class named Bike. In the class Bike we have created two static methods named start and stop. Then we have created a class named Kawasaki that inherits the properties of the class Bike. In the class Kawasaki we have created a constructor that takes one argument brand. Then we have created a class named Ninja that inherits the properties of the class Kawasaki. In the class Ninja we have created a constructor that takes one argument model. Then we have created three objects of the class Ninja and printed the model attribute of the object bike1. Then we have called the start method using the object bike1. It will print the model attribute of the object bike1 and then it will print Bike has started. It will print None because the start method does not return anything. 


"""
# 3. Multiple Inheritance

    Multiple inheritance is the process by which one class(child/derived) derives the properties of more than one class(parent/base) then it is called multiple inheritance.
    
"""
# Example:

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varA) # it will print the varA attribute of the object c1.
print(c1.varB) # it will print the varB attribute of the object c1.
print(c1.varC) # it will print the varC attribute of the object c1.

# So the above code is the example of multiple inheritance.

# Super() method in python
# super() method is used to call the constructor of the parent class.
# super() method is used to access the methods of the parent class.

# Example:
class A:
    def __init__(self):
        print("Constructor of class A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor of class B")

b1 = B()



