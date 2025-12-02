#!/usr/bin/python3

"""Dictionaries in Python"""

print("===Dictionaries===")
# Creating dictionaries 
# Using curly braces
county_gov = {
        "Kisumu": "Prof. Anyang' Nyong'o",
        "Nairobi": "Johnson Sakaja",
        "Mombasa": "Abdulswamad Shariff",
        "Machakos": "Wavinya Ndeti",
        "Kitui": "Dr.Julius Malombe",
        "Trans Nzoia": "George Natembeya"
        }

# using dict() function
identity_matrix = dict(x=1, y=0, w=1, z=0)

print("County-Gov: ", county_gov)
print("Identity_Matrix: ", identity_matrix)

print("===Accessing values in a dictionary===")
# using []
ksg = county_gov["Kisumu"]
ng = county_gov["Nairobi"]
mog = county_gov["Machakos"]

# using get() method 
mag = county_gov.get("Machakos")
ktg = county_gov.get("Kitui")
tg = county_gov.get("Trans Nzoia")

print("Kisumu Governor: ", ksg)
print("Nairobi Governor: ", ng)
print("Mombasa Governor: ", mog)
print("Machakos Governor: ", mag)
print("Kitui Governor: ", ktg)
print("Trans Nzoia: ", tg) 

print("===Modifying values in a dictionary===")
# Updating a dictionary 
# using the square brackets []
county_gov["Kisumu"] = "Anyang' Nyong'o"
new_ksg = county_gov["Kisumu"]
# using update () method 
county_gov.update({"Kitui": "Julius Malombe"})
new_ktg = county_gov["Kitui"]
county_gov.update({"Homabay": "Gladys Wanga","Kisii": "Simba Arati"})
print("New Kisumu Governor: ", new_ksg)
print("New Kitui Governor: ", new_ktg)
print("New_dictionary: ", county_gov)

print("===Deleting/removing elements from a dictionary===")
# del keyword
del county_gov["Homabay"]
print("County_gov after deleting Homabay: ", county_gov)
#using pop()
county_gov.pop("Kisii")
print("County_gov after removing Kisii: ", county_gov)
# using popitem()
county_gov.popitem()
print("County_gov after removing Trans Nzoia: ", county_gov)
# using clear()
identity_matrix.clear()
print("Identity_matrix after removing all elements-empty dictionary: ", identity_matrix)

print("===Dictionary Methods===")
print("Keys: ", county_gov.keys())
print("Values: ", county_gov.values())
print("Items: ", county_gov.items())
county_gov2 = county_gov.copy()
print("A copy of county_gov: ", county_gov2)
