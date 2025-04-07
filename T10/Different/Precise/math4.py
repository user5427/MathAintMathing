import math


a = 5.7
q = 1.39

c = 4 * a * a - 12 * q * q
bx = -8 * a
ax = 4

D = bx * bx - 4 * ax * c
if D < 0:
    print("No solution")
else:
    u1 = (-bx + math.sqrt(D)) / (2 * ax)
    u2 = (-bx - math.sqrt(D)) / (2 * ax)

    v1 = 2*a - u1
    v2 = 2*a - u2
    
    print(f"u1 = {u1}, v1 = {v1}")
    print(f"u2 = {u2}, v2 = {v2}")    