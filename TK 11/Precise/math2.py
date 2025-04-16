N = 57
k = 15
n = 5

sumOfProbs = (N - k) / N
for i in range(1, n):
    prob = (N - k - i) / (N - i)
    
    sumOfProbs *= prob
    
print(f"Probability: {1 - sumOfProbs}")