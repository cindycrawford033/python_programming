#!/usr/bin/python3

"""recursive function"""


def factorial(n):
     """This function returns factorial of a number"""
     if n == 0 or n == 1:
         return  1
     else:
         return n * factorial(n -1)


result = factorial(3)
print ("factorial: ", result)           
