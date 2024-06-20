# Create student class that takes name and marks of three subjects as argurements in constructor Then create a method that prints the average of three subjects.

class Student:
    def __init__(self,name, marks): 
        self.name = name
        self.marks = marks
    def get_average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your average marks is: ", sum/3)


s1 = Student("karan", [98, 97, 96])
s1.get_average()
