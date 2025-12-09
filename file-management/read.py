#!/usr/bin/python3

"""Reading files using read(), readline(), readlines()"""

"""Using open() function to read a file"""
file = open("stats.txt", "r", encoding="utf-8")
print(file.read())
print(file.closed)
file.close()
print(file.closed)

"""Using with statement in conjunction with open()"""
with open("stats.txt", "r", encoding="utf-8") as file:
    print(file.read())
print(file.closed)

"""using readline()"""
with open("stats.txt", "r" , encoding="utf-8") as file:
    line = file.readline()
    while line: 
        print(line, end="")
        line = file.readline()

"""Using readlines()"""
with open("stats.txt" , "r", encoding="utf-8") as file:
    lines = file.readlines()
    for lne in lines:
        print(line, end="")
