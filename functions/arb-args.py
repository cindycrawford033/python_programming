#!/usr/bin/python3

"""function with arbitrary arguments"""


def sum_all(*args):
    """This function returns the sum of all arguments passed by the user"""
    result = sum(args)
    return result


def add_numbers(*num):
    output = 0
    for i in num:
        output += i
    return output


result = sum_all(20, 40, 60, 80, 100, 120, 140, 160, 180, 200)
output = add_numbers(20, 40, 60, 80, 100, 120, 140, 160, 180, 200)
print("sum_all: ", result)
print("add_numbers: ", output)
