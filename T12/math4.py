Q = 0.95
e = 0.06

e = e/2

n = 1/(e**2*(1-Q)*4)
print(f"Minimum number of mushrooms needed: {n}")
print(f"Rounded up to whole number: {int(n) + 1}")  # Need at least ceil(n) mushrooms