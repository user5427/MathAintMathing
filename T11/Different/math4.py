x ="EBCBBCCACCCCBCC"
x = list(x)

# find qunique letters
unique = 5

occurences = {}
for i in x:
    if i in occurences:
        occurences[i] += 1
    else:
        occurences[i] = 1
        
        
f = {}
for i in occurences:
    fi = occurences[i] / len(x)
    f[i] = fi
    
variability = unique / (unique - 1)
sum = 1
for i in f:
    sum -= f[i] ** 2
variability *= sum
print(f"Variability = {variability}")


# architekturiniai paternai ir stiliai priklauso nuo funkciniu reikalavimu. pereiti pro nefunkcinius reikalavimus ir pasirasyti keleta funkciniu reikalavimu.
# skaitoma pipeline pataginti.