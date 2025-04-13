λ1 = 0.54
λ2 = 0.37

AWait = 1 / (λ1 + λ2)

BWait = λ1 / (λ1 + λ2) * (1 / λ2) +   λ2 / (λ1 + λ2) * (1 / λ1)

print(AWait)
print(AWait + BWait)