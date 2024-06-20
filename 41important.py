# Four Pillars of Object Oriented Programming
# 1. Abstraction - Hiding the complex details and showing only the necessary things.
# Hiding the implementation details of a class and only showing the necessary things to the user.

# Example:

class Car:
    def __init__(self):
        self.accelrator = False
        self.brake = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.accelrator = True
        print("Car has started")

car1 = Car()
car1.start()
        
