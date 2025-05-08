x = [1.6, 4.4, 3.4, 3.1, 0.8, 2.5, 2.9, 2.6, 2.8, 3.2]
y = [3.9, 6.4, 5.6, 5.3, 2.2, 2.6, 3.7, 3.4, 3.4, 5.3]

xAvr = sum(x) / len(x)
yAvr = sum(y) / len(y)

xDisp = sum([(i - xAvr) ** 2 for i in x]) / (len(x) - 1)
yDisp = sum([(i - yAvr) ** 2 for i in y]) / (len(y) - 1)
xDisp = xDisp ** 0.5
yDisp = yDisp ** 0.5

R = 1 / (len(x) - 1) * sum(x[i] * y[i] for i in range(len(x))) - xAvr * yAvr * len(x) / (len(x) - 1)
R = R / (xDisp * yDisp)
print(f"R = {R}")
