#!/usr/bin/python3

"""Classes and Objects"""

class Reptilia:
    def __init__(self, name, age, habitat, meal):
        """Instance attributes/instance(object) variables"""
        self.name = name
        self.age = age
        self.habitat = habitat 
        self.meal = meal 

        """instance/object methods"""
    def swim(self):
        print (f"{self.name} is very swift in {self.habitat}, please take care!")

    def predator(self):
        print("{} is an apex preditor in {} and its favorite meal is {}.". format(self.name, self.habitat, self.meal))
   
    def bask(self):
        print(f"{self.name} are poikilotherms and do bask on shores to radiate.")
    
    def __str__(self):
        return f"My favourite reptile is {self.name} and aged {self.age} years old."


# user input to create an object 
rept = input("What's the name of your favorite reptile?: ")
aging = int(input("How old do you think this reptile is?: "))
habit = input (" What's the habitat of this reptile?: ")
meel = input("What's the favorite meal of this reptile? ")

# Creating the object 
reptile = Reptilia (rept, aging, habit, meel)

# Accessing object attributes 
print("Nmae: ", reptile.name)
print("Age: ", reptile.age)
print("Habitat: ", reptile.habitat)
print("Meal: ", reptile.meal)

# Accessing object methods 
reptile.swim()
reptile.predator()
reptile.bask()

# Accessing object using str()
print(reptile)
