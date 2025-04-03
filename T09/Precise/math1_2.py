a = 11.0
b = 5.0
x = 2.21 

# D[\(40)Divide[\(40)b*Divide[a,2]-Divide[\(40)b-x\(41)*a,b]*Divide[\(40)b-x\(41),2]\(41),b*Divide[a,2]]\(41),x]

der = 2 * (b - x) / b ** 2
print(der)