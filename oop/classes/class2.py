#!/usr/bin/python3 

"""classes and objects"""
class Dog:
    def __init__(self, name, breed, age, color):
        """instance attributes"""
        self.name = name 
        self.breed = breed 
        self.age = age 
        self.color = color 

        """Object methods"""
    def bark(self):
        print(f"{self.breed} breeds bark the loudest")
        
    def run(self):
        print("{} breeds with age lower than {} years are the fastest." .format(self.breed, self.age))
        
    def aesthetic(self):
        print(f"{self.breed} with {self.color} are very attractive")

    def hunting(self):
        print("{} breeds are very active in hunting.".format(self.breed))

    def naming(self):
        print(f"Dogs with {self.name} names are aggressive, please avoid them!.")

# Taking user input 
dog1 = input("what's the name of your dog?: ")
dog2 = input("what's the breed of your dog?: ")
dog3 = int(input ("How old is your dog?: "))
dog4 = input("what's the colour of your dog?: ")

# Creating object 
dog = Dog(dog1, dog2, dog3, dog4)

#Accessing object attributes 
print("Name: ", dog.name)
print("Breed: ", dog.breed)
print("Age: ", dog.age)
print("Color: ", dog.color)

# Accessing object methods 
dog.bark()
dog.run()
dog.aesthetic()
dog.hunting()
dog.naming()
