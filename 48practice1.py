# Define a Circle class to create a circle with radius r using the constructor 
# Define an Area() method of the class which calculates the area of the circle
# Define a Perimeter() method of the class which calculates the perimeter of the circle

class Circle:
    def __init__(self, r):
        self.radius = r

    def Area(self):
        return 3.14 * self.radius ** 2
    
    def Perimeter(self):
        return 2 * 3.14 * self.radius


c1 = Circle(7)
print("Area of the circle is: ", c1.Area())
print("Perimeter of the circle is: ", c1.Perimeter())

# Output: Area of the circle is:  153.86
#         Perimeter of the circle is:  43.96

# Explanation: In the above code we have created a class named Circle. In the class Circle we have created a constructor that takes one argument r. Then we have created a method named Area that calculates the area of the circle. Then we have created a method named Perimeter that calculates the perimeter of the circle. Then we have created an object of the class Circle and called the Area method using the object of the class Circle. Then we have called the Perimeter method using the object of the class Circle. It will print the area and perimeter of the circle. 