x = [6.6, 8.7, 9.9, 8.8, 9, 1, 0.4, 6.6, 5.7, 8.4]
p = 30

p = p / 100

avg = sum(x) / len(x)
# print(avg)

dispersion1 = sum([(i - avg) ** 2 for i in x]) / (len(x) - 1)
# print(f"{dispersion} not squared")

y = (1+p) * avg * (len(x) + 1) - sum(x)

print(y)
x.append(y)

avg = sum(x) / len(x)
# avg *= (1+p)
# print(avg)

dispersion2 = sum([(i - avg) ** 2 for i in x]) / (len(x) - 1)
# print(f"{dispersion} not squared")


print(dispersion2 - dispersion1)