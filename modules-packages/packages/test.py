#!/usr/bin/python3

"""importing modules"""
from mypackage.calculator import add, sub, mul, div, exp, factorial

print("===Testing my calculator===")
a = int(input("Enter the value of a: "))
b = int(input("Entger the value of b: "))
n = int(input("Enter the number to get the factorial: "))

print(f"The sum of {a} and {b} is: ", add(a, b))
print(f"The difference of {a} and {b} is: ", sub(a, b))
print(f"The product of {a} and {b} is: ", mul(a, b))
print("The quotient of {} and {} is: ".format(a, b), div(a, b))
print("The exponent of {} and {} is: ".format(a, b), exp(a, b))
print("The factorial of {} is: ".format(n), factorial(n))
