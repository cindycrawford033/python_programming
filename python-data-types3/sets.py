#!/usr/bin/python3

"""Sets"""

# methods of creating sets
# using curly braces 

print("===Creating sets===")
s1 = {2, 5, 6, 7}

# using set() constructor
s2 = set([1, 3, 5, 7, 9])

s3 = set((20,40,50,70))
print("s1: ", s1)
print("Class of s1: ",type(s1))
print("s2: ", s2) 
print("Class of s2: ", type(s2))
print("s3: ", s3)
print("Class of s3: ", type((s3)))

print("====Set Methods===")
# Adding an element
s1.add(11)
print("Updated s1: ", s1)

# Clearing elements from a set
s3.clear()
print("Cleared s3 - should be an empty set: ", s3) 

# Making a shaloow copy of the original set 2
s4 = s2.copy()
print("Copy of s2: ", s4)

# Discarding elements from a set
s2.discard(7)
print("Discarded s2: ", s2)

# Popping elements from a set
s1.pop()
print("Popped s1: ", s1)

#Removing elements from a set 
s5 = {20, 40, 60, 80}
print("s5: ", s5)
s5.remove(20)
print("Modified s5: ", s5) 


print("===Set Operations===")
set1 = {1, 3, 5, 7, 9}
set2 = {2, 4, 6, 8, 10}
print("Set1: ",set1)
print("Set2: ", set2)
#set union
# or operator 
set3 = set1 | set2
print("set1 union set2-using | operator: ", set3)
set4 = set1.union(set2)
print("Set1 union set2-using union function: ", s4)

# set intersection 
set5 = {2, 4, 6, 8}
set6 = {2, 4, 9, 10}
print("set5: ", set5)
print("Set6: ", set6)
set7 = set5 & set6
set8 = set5.intersection(set6)
print("Set intersection set6 - using & operator: ", set7)
print("Set5 intersection set6 - using intersection function: ", set8)

#Set difference
set9 = {1, 3, 5, 7}
set10 = {1, 3, 9, 11}
print("Set9: ", set9)
print("Set10: ", set10)
set11 = set9 - set10
set12 = set9 - set10
print("Set9 difference set10- using minus operator: ", set11)
print("Set9 difference set10 - using difference function: ", set12)

# set symmetric difference 
set13 = {1, 3, 5, 7, 9}
set14 = {1, 5, 8, 10, 12}
print("Set13: ", set13)
print("Set14: ", set14)
set15 = set13 ^ set14
set16 = set13.symmetric_difference(set14) 
print("set13 symmetric difference set 14-using ^ operator: ", set15)
print("set13 symmetric difference set14-using symmetric difference function: ", set16)
