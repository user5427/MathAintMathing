a = 5
b = 3
x = 1.62

DE = (a-x) / a * b
AD = a - x

Sbdec = b * a / 2 - DE * AD / 2
Sabc = b * a / 2

prob = Sbdec / Sabc
print(prob)


# D[\(40)Divide[\(40)b*Divide[a,2]-Divide[\(40)b-x\(41)*a,b]*Divide[\(40)b-x\(41),2]\(41),b*Divide[a,2]]\(41),x]

der = (2 * (a - x)) / a ** 2
print(der)