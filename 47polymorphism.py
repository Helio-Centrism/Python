# Polymorphism : Operator Overloading
# Polymorphism is an ability to use common interface for multiple data types.
# Operator Overloading(is the best example for polymorphism) is a type of polymorphism in which an operator is overloaded to give user defined meaning to it.
# When the same operator is allowed to have different meaning according to the context then it is called operator overloading.

# Example: 
print(5 + 6)  # it will add 5 and 6 and print the result.
print(type(5))
print("hello" + "world")  # it will concatenate the two strings and print the result.
print(type("hello"))
print([1, 2, 3] + [4, 5, 6])  # it will concatenate the two lists and print the result(merge)
print(type([1, 2, 3]))
# this is an implicit operator overloading because the + operator is overloaded to give different meanings according to the context.

# In the above code we have used the + operator to add two numbers, concatenate two strings, and concatenate two lists. So the + operator is overloaded to give different meanings according to the context. This is an example of operator overloading.

# Operators and Dunder Functions
# In Python, operator overloading is done by defining special functions in the class. These special functions are also called dunder functions. Dunder functions are the functions that start and end with double underscores. These functions are automatically called when a specific operation is performed on the object of the class.

# Example: we will create a complex class

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def showNumber(self):
        print(f"{self.real}i + {self.imag}j")

num1 = Complex(3, 4)
num1.showNumber()

num2 = Complex(5, 6)
num2.showNumber()

# so to add two complex numbers we have to define a special function in the class Complex because the + operator is not defined for the class Complex which we have created so to do such task we have dunder function .

# Output: 3i + 4j
#         5i + 6j

# Explanation: In the above code we have created a class named Complex. In the class Complex we have created a constructor that takes two arguments real and imag. Then we have created a method named showNumber that prints the real and imag attributes of the object. Then we have created two objects of the class Complex and called the showNumber method using the objects of the class Complex. It will print the real and imag attributes of the objects. 

#*********************************************************************************************************************************************************************

# Dunder Functions for Operator Overloading
# In Python, operator overloading is done by defining special functions in the class. These special functions are also called dunder functions. Dunder functions are the functions that start and end with double underscores. These functions are automatically called when a specific operation is performed on the object of the class.
"""
#  a + b  # addition  a__add__b
#  a - b  # subtraction  a__sub__b
#  a * b  # multiplication  a__mul__b
#  a / b  # division  a__truediv__b
#  a // b  # floor division  a__floordiv__b
#  a % b  # modulus  a__mod__b
#  a ** b  # power  a__pow__b
#  a += b  # addition  a__iadd__b

"""
# Example: we will create a complex class

class Complex:
    
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def showNumber(self):
        print(f"{self.real}i + {self.imag}j")

    def __add__(self, other):
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return Complex(new_real, new_imag)
    # so here we have defined a special function __add__ that takes two arguments self and other. Then we have created two new variables new_real and new_imag that stores the sum of the real and imag attributes of the objects. Then we have created a new object of the class Complex and returned the object. 
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    # so here we have defined a special function __sub__ that takes two arguments self and other. Then we have created a new object of the class Complex and returned the object.
    

num1 = Complex(32, 4)
num1.showNumber() # 32i + 4j

num2 = Complex(5, 6)
num2.showNumber()   # 5i + 6j

num3 = num1 + num2
num3.showNumber() # 37i + 10j because 32+5 = 37 and 4+6 = 10 

num4 = num1 - num2
num4.showNumber() # 27i - 2j because 32-5 = 27 and 4-6 = -2

