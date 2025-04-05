a = 13
b = 20
x = 7.2

DE = (a-x) / a * b
AD = a - x

Sbdec = b * a / 2 - DE * AD / 2
Sabc = b * a / 2

prob = Sbdec / Sabc
print(prob)


# D[\(40)Divide[\(40)b*Divide[a,2]-Divide[\(40)b-x\(41)*a,b]*Divide[\(40)b-x\(41),2]\(41),b*Divide[a,2]]\(41),x]

der = (2 * (a - x)) / a ** 2
print(der)