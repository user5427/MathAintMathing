m = 99
n = 1506
p = 7
q = 3


difference = (n - m)
pProb = ((difference) / p) / difference
qProb = ((difference+3) / q) / difference

prob = pProb + qProb - (pProb * qProb) # 21 is the LCM of 7 and 3 so dont forget to subtract the intersection
print(f"Probability: {prob}")



pCount = 0
qCount = 0
for i in range(m, n+1):
    if i % p == 0:
        pCount += 1
    if i % q == 0:
        qCount += 1
        
pProb = pCount / (n - m)
qProb = qCount / (n - m)


print(qCount)
print(pCount)
print(difference // p)
print(difference // q)

prob = pProb + qProb - (pProb * qProb) # 21 is the LCM of 7 and 3 so dont forget to subtract the intersection
print(f"Probability: {prob}")