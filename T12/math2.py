# https://youtu.be/bObW7lhDwKs?list=PLk_RB-ywjAuNChB0-dly51Dgx0p51PGYE&t=966
m = [9, 10, 10, 12, 8, 11, 8, 10, 10, 8, 6, 7, 11, 8, 9, 8, 6, 10, 11, 9, 11, 10, 9, 10, 6, 4, 7, 8, 7, 10, 8]

n = len(m)
a1 = sum(m) / n
a2 = sum(i ** 2 for i in m) / n

# Estimate probability of success using method of moments
p = 1 - ((a2 - a1**2) / a1)

# Estimate original team size
k = a1 / p

# Calculate hole diameter (in meters)
# If road is 1m wide and success probability is p,
# then hole diameter = (1-p) meters assuming uniform distribution
hole_diameter = 1 - p

print(f"Sample mean (a1): {a1:.4f}")
print(f"Sample second moment (a2): {a2:.4f}")
print(f"Estimated command size (k): {k:.4f}")
print(f"Estimated probability of success (p): {p:.4f}")
print(f"Estimated hole diameter: {hole_diameter:.4f} meters")