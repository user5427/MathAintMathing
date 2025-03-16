pA = 0.33
pB = 0.64

# set to true if pralaimes
invert = False

if invert:
    pA = 1 - pA
    pB = 1 - pB

sum = 0

sum = pA * pB * pA + pA * pB * (1 - pA) + pA * (1 - pB) * pA + (1 - pA) * pB * pA + (1 - pA) * pB * (1 - pA)

print(sum)