p = 51
q = 69
k = 6

p = p / 100
q = q / 100


oneGud = 1 - (1 - p) * (1 - q)

Z = k * (1 - oneGud) / oneGud
# print(Z)
print(Z + k)