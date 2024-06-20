# Define a Employee class with attributes role, department, salary . This class should also have a showDetails() method. Create an Engineer class that inherits the Employee class and has an additional attribute called name and age

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Role: ", self.role)
        print("Department: ", self.department)
        print("Salary: ", self.salary)

E1 = Employee("Software Engineer", "IT", 50000)
E1.showDetails()

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("AI Engineer", "R&D", 600000)

Eng1 = Engineer("Vaibhaav", 21)
Eng1.showDetails()
