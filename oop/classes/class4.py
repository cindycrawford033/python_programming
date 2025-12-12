#!/usr/bin/python3

"""Class variables"""

class Animalia:
    # class variable
    division = "chordata"

    def __init__(self, name, age, color):
        #instance attributes/variables 
        self.name = name 
        self.age = age
        self.color = color 

    # Object methods 
    def hunting(self):
        print(f"{self.name} is a vicious predator for mice.")

    def purring(self):
        print("Meow, meow!")

    def safeguarding(self):
        print("{} with {} color is  very protective." .format(self.name, self.color))

# Taking user input to create an object
chord = input("What's your favorite pet?: ")
aging = int(input("How old is your pet?: "))
collor = input("What's the color of your pet?: ")

# Creating the object 
cat = Animalia(chord, aging, collor)

# Accessing the object attributes 
print("Name: ", getattr(cat, "name"))
print("Age: ", getattr(cat, "age"))
print("Color: ", getattr(cat, "color"))

#Accessing the object methods
cat.hunting()
cat.purring()
cat.safeguarding()

print("Cat division: ", cat.division)
# Accessing the class variable 
print(f"Original class variable of the class is {Animalia.division}.")
# Modifying class variable for the object
cat.division = "vertebrates"
print("The current class variable is {}.".format(cat.division))
# Modifying class variable for the class
Animalia.division = "Vertebrate"
print("The current class variable of the class is {}.".format(Animalia.division))
