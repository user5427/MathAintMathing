from My_Probability.count_calculators import C


white = 24
black = 11
n = 8
k = 9

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
