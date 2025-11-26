#!/usr/bin/python3

# string operations 

str1 = "Python is fun"
str2 = "and it is a high level programming language."
str3 = "It was pioneered by Guido Van Rossum."
str4 = ["Python", "is", "fun"]

print("===String Operations===")

print(str1)
print(str2)
print(str3)
print(str4)

print("Concatenation:", str1 + str2 + str3)

print("Repetition: ", str1 * 2)

# Indexing and slicing 
print("===Indexing and slicing===")
print("Positive Indexing: ", str1[3])
print("Negative Indexing: ", str1[-1])
print("Slicing: ", str3[19:35])

# String methods 
print("===String methods===")
print("Uppercase: ", str1.upper())
print("Lowercase: ", str1.lower())
print("Endswith: ", str1.endswith("Rossum"))
print("Isalpha: ", str2.isalpha())
print("Join: ", " ". join(str4))
print("Strip: ", str1.strip())

# String formatting 
print("===String formatting methods===")
price = 220
country = "UK"
# using f-strings
print(f"The price of a laptop in {country} is {price} dollars.")
print("The price of a laptop in {} is{} dollars.".format(country, price))

lang = "Python"
print(f"The easiest programming langauge to learn is {lang}.")
print("The easiest programming language to learn is {}.".format(lang))
