a = 0.4
b = 3
n = 9

nDividers = [1, 3, 9]

def eXm(m):
    #  (b^(m+1) - a^(m+1))/((m+1)(b-a))
    return (b**(m+1) - a**(m+1)) / ((m+1)*(b-a))

sum = 0
for i in range(len(nDividers)):
    sum += (nDividers[i]**-2) * eXm(nDividers[i])
    
print(sum)