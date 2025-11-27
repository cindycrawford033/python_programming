#!/usr/bin/python3

# lists 
# creating lists using square brackets[]
x = [20, 30, 40, 50]
y = ["apple", "banana", "mango"]
n = [1, 2, 3, 4, 5]
# using list() constructor 
w = list((20, 20, 20, 60))
v = list({"Arsenal", "Chelsea", "Liverpool"})
# list operations
print("===List Operations===")
print("x: ", x)
print("y: ", y)
print("w: ", w)
print("v: ", v)
print("n: ", n)
# indexing 
print("Positive indexing: ", x[2])
print("Negative indexing: ", x[-2])

# slicing 
print("Slicing: ", x[1:3])

# Updating(mutability)
x[3] = 60

# joining lists with + operator 
print("Joining x and y: ", x + y)

# list methods 
print("===List Methods===")
print("x: ",x)
x.append(70)
print("Append: ", x)
v.clear()
print("Clear: ", v)
p = y.copy()
print("Copy:", p)
print("Count: ", w.count(20))
x.extend(y)
print("x: ", x)
print("Index: ", w.index(60))
w.insert(4, 70)
print("w: ", w)
print("Pop: ", y.pop(2))
print("y: ", y)
p.remove("banana")
print ("Remove: ", p)
n.reverse()
print("Reverse: ", n)
m = [50, 30, 70, 10]
print("m: ", m)
m.sort()
print("Sort: ", m)
