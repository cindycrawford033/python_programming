#!/usr/bin/python3


"""modules"""


def add(a,b):
    """This function returns sum of a and b"""
    res = a + b
    return res


def sub(a,b):
    """This function returns the difference between a and b"""
    res = a - b
    return res


def mul(a,b):
    """This function returns the product of a and b"""
    res = a * b
    return res


def div(a,b):
    """This function returns the quotient of a and b"""
    res = a/ b
    return res


def exp(a,b):
    """This function returns the exponent of a and b"""
    res = a ** b 
    return res


def factorial(n):
    """This function returns the factorial of a number"""
    if n == 0 or n == 1:
        return 1
    else: 
        return n * factorial(n - 1)
