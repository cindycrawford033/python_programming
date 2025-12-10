#!/usr/bin/python3

"""classes and objects"""

class Car:
    def __init__(self, make, model, year):
        """instance/object attributes"""
        self.make = make
        self.model = model
        self.year = year

        """object methods"""
    def race(self):
        print("{} is best for racing.".format(self.make))

    def hoot(self):
        print("Beep! Beep!")

    def transporter(self):
        print(f"The {self.make} cars are suited for transportation.")

# creating the object-instance of a class
car1 = Car("BMW", "x6", 2025)

# Accessing object attributes 
print("make: ", car1.make)
print("model: ", car1.model)
print("year: ", car1.year)

# Accessing the object methods 
car1.race()
car1.hoot()
car1.transporter()
