m = 99
n = 1506
p = 7
q = 3


difference = (n - m)
pProb = (difference // p) / difference
qProb = (difference // q) / difference

prob = pProb + qProb - (pProb * qProb) # 21 is the LCM of 7 and 3 so dont forget to subtract the intersection
print(f"Probability: {prob}")