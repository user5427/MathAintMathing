Q = 0.95
e = 0.06


n = 1/(4*e**2*(1-Q))
print(f"Minimum number of mushrooms needed: {n}")
print(f"Rounded up to whole number: {int(n) + 1}")  # Need at least ceil(n) mushrooms