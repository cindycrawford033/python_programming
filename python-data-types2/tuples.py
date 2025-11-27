#!/usr/bin/python3

# tuples

# using parentheses()
x = ("Nairobi", "Mombasa", "Machakos", "Kisumu", "Uasin Gishu")

y = ("Arsenal", 13, "Man U", 20, "Real Madrid", 15)

#creating singleton tuple, must have a trailing comma.
s = "Homabay"
v = "Homabay", 
t = 12,
w = 12

# using  tuple() constructor
n = tuple([1, 2, 3, 4, 5])
m = tuple({20, 40, 50, 60})
k = tuple("Python")

# creating empty tuples using parentheses
p=()

# creating empty tuple using tuple() constructor
q = tuple()

print("===printing tuples and their classes===")
print("x: ", x)
print("class of x: ", type(x))
print("y: ", y)
print("class of y: ", type(y))
print("s: ", s)
print("class of s: ", type(s))
print("v: ", v)
print("class of v: ", type(v))
print("t: ", t)
print("class of t: ", type(t))
print("w: ", w)
print("class of w: ", type(w))
print("n: ", n)
print("class of n: ", type(n))
print ("m: ",m)
print("class of m: ", type(m))
print("k: ", k)
print("class of k: ", type(k))
print("p: ", p)
print("class of p: ", type(p))
print("q: ", q)
print("class of q: ", type(q))



# Tuple operations
print("===Tuple Operations===")
# indexing
t1 = (20, 40, 60, 80, 100)
print("t1: ", t1)
print("Positive Indexing: ", t1[3])
print("Negative Indexing: ", t1[-2])

# Slicing variablename[x:y]
print("Slicing: ", t1[1:4])

t2 = (120, 140, 160, 180, 200)
# concatenation using + operator
print("t2: ", t2)
print("Concatenation of t1 and t2 is: ", t1 + t2)
#repetition using * operator
print("Repetition of t1: ", t1 * 2)

# deleting a tuple 
animals = ("dog", "cat", "rabbit")
print("Animals: ", animals)
del animals

# Tuple functions
print("===Tuple functions===")
# len()-gives length of an iterable 
print("t1: ",t1)
print("length of t1: ", len(t1))
# checking max and min in an iterable
print("Max value in t1: ", max(t1))
print("Min value in t1: ",min(t1))

# Tuple methods 
t3 = (20, 30, 30, 30, 50)
print("===Tuple methods===")
print("t3: ", t3)
print("Count how many times 30 appears in t3: ", t3.count(30))
print("Index of 50 in t3: ", t3.index(50))
