#!/usr/bin/python3

"""Multiple inheritance"""
# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hi, {self.name}. How are you doing?")


# Base class
class Student:
    def __init__(self, student_id, course, university):
        self.student_id = student_id
        self.course = course
        self.university = university

    def enroll(self):
        print(f"{self.name} with student id: {self.student_id} has enrolled for {self.course} at {self.university}.")

    def study(self):
        print(f"{self.name} is studying {self.course} at {self.university}.")


# Derived class using multiple inheritance
class Teacher(Person, Student):
    def __init__(self, name, age, student_id, course, university, tsc_no, subjects, school):
        # Initialize parent classes
        Person.__init__(self, name, age)
        Student.__init__(self, student_id, course, university)
        
        # Teacher-specific attributes
        self.tsc_no = tsc_no
        self.subjects = subjects
        self.school = school

    def teach(self):
        print(f"{self.name} teaches {self.subjects} at {self.school}.")

    def coach(self):
        print(f"{self.name} coaches students at {self.school}.")


# Create an instance of Teacher
teacher = Teacher(
    "Kafengo", 25, "STA4502025", "Statistics", "Kenyatta University",
    "TSC4502025", "Maths and Chem", "Mwerevu School"
)

# Accessing teacher attributes
print("Name: ", teacher.name)
print("Age: ", teacher.age)
print("Student ID: ", teacher.student_id)
print("Course: ", teacher.course)
print("University: ", teacher.university)
print("TSC NO: ", teacher.tsc_no)
print("Subjects: ", teacher.subjects)
print("School: ", teacher.school)

# Calling teacher methods
teacher.say_hello()   # From Person
teacher.enroll()      # From Student
teacher.teach()       # From Teacher
teacher.coach()       # From Teacher
teacher.study()       # From Student
