#!/usr/bin/python3

"""for loop"""
print("===for loop===")
m = [1, 2, 3, 4, 5]

for  i in m:
    print("i: ", i)

for i in m:
    if i % 2 == 0:
        continue 
    print("i: ", i)

for i in m:
    if i ==3:
        break
    print("i: ", i)
for k in range(10):
    print("k: ", k)

for t in range(1, 10):
    if t % 2 == 0:
        continue
    print("t: ",t)
