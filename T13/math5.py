# Duota dvimačio atsitiktinio dydžio (X, Y) imtis (2.6, 4.6); (3.4, 2.7); (4.4,
# 3.8); (4.8, 5.1); (3.2, 2.6); (3, 3.5); (4.3, 4.2); (4, 7.8); (3.4, 4.4)
# Patikrinkite hipotezę, kad X ir Y yra nekoreliuojantys dydžiai. Pateikite
# gautąją p-reikšmę.

from scipy.stats import t, pearsonr

X = [2.6, 3.4, 4.4, 4.8, 3.2, 3, 4.3, 4, 3.4]
Y = [4.6, 2.7, 3.8, 5.1, 2.6, 3.5, 4.2, 7.8, 4.4]

xAvr = sum(X) / len(X)
yAvr = sum(Y) / len(Y)

xyMult = sum(X[i] * Y[i] for i in range(len(X)))

xDisp = sum((i - xAvr) ** 2 for i in X) / (len(X) - 1)
yDisp = sum((i - yAvr) ** 2 for i in Y) / (len(Y) - 1)

xDisp = xDisp ** 0.5
yDisp = yDisp ** 0.5

r = xyMult - len(X) * xAvr * yAvr
r = r / ((len(X) - 1) * xDisp * yDisp)

tr = r * (((len(X) - 2) / (1 - r ** 2)) ** 0.5)

Pr = 2 * (1 - t.cdf(abs(tr), len(X) - 2))

print(f"p-value for H₁: X and Y are not independent is {Pr}")

# r, Pr = pearsonr(X, Y)
# print(f"r = {r}")
# print(f"p-value for H₀: X and Y are uncorrelated is {Pr}")