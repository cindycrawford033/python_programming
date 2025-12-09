#!/usr/bin/python3

"""writing files in python using write(), writelines()"""
with open("epi.txt", "w", encoding="utf-8") as file: 
    file.write("Hi Mwende, how is network on your side?\n")

"""Appending content to a file"""
with open("epi.txt", "a", encoding="utf-8") as file:
    file.write("You need to change your location.\n")
