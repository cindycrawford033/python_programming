#!/usr/bin/python3

""" inheritance using super() method (super().__init__)"""

# parent class
class Animals:
    def __init__(self, name, species):
        self.name = name 
        self.species = species 

    def move(self):
        print(f"{self.name} is migratory if not well fed.")


# child class
class Dog(Animals):
    def __init__(self, name, age, breed, color):
        # initializing object attributes by calling super() 
        # when using duper(), we dont pass self in the __init__()
        super().__init__(name, species="Dog") 
        self.age = age 
        self.breed = breed
        self.color = color 
    
    #overiding parent method
    def move(self):
        print("{} is very homy when taken care of.".format(self.name))

    def hunting(self):
        print(f"{self.breed} breeds are very vicious hunters.") 

    def bark(self):
        print("Dogs with {} color aged {} years old are loud when barking.".format(self.color, self.age))

# creating dog object 
dog = Dog("finisher", 2, "German Shepherd", "White")

# Accessing dog attributes 
print(dog.species)
print(dog.age)
print(dog.breed)
print(dog.color)

# Calling overriden method move 
dog.move()

# calling child class(dog) methods 
dog.hunting()
dog.bark()
