from My_Probability.count_calculators import C


white = 5
black = 10
n = 7
k = 4

def calculate(n, k, prob):
    negProb = 1 - prob
    return C(n, k) * (prob ** k) * (negProb ** (n - k))
    

sum = 0
for i in range(0, n):
    x = calculate(n, i, white / (white + black))
    y = calculate(i, 0, white / (white + black))
    print(x, y)
    sum += x * y
    
print(sum)
