#!/usr/bin/python3

"""while loop"""
print("===while loop===")
n = 0
while n < 10:
    print("n: ", n)
    n += 1

m = 0
while True:
    if m == 5:
        break
    print("m: ", m)
    m += 1

i = 0
while i <= 5:
    print("i: ", i)
    i += 1
else:
    print("Done printing")

k = 0
while k < 10:
    if k % 2 == 0:
        k += 1
        continue
    print("k: ", k)
    k += 1
