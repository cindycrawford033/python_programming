#!/usr/bin/python3

"""function with default arguments"""


def hello(name, age=25):
    """This function greets and tells the user his or her name"""
    print("Hello {}.You are {} years old.".format(name, age))


hello("Mwende")
