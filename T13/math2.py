# Televizijų žaidimuose dalyvauja P% moterų. Patikrinkite hipotezę, kad moterims
# sekasi taip pat gerai kaip ir vyrams su alternatyva, kad joms sekasi geriau,
# jeigu iš n laimėtojų moterų buvo m. Pateikite gautąją p-reikšmę. ( P = 38 , n
# = 9 m = 6 )
from math import comb

P = 38
n = 9
m = 6

p0 = P / 100

def binom_pmf(n, k, p): # B(n,k,p0) kad taip pat sekasi gerai kaip ir vyrams
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

def binom_cdf(n, k, p):
    return sum(binom_pmf(n, i, p) for i in range(k + 1))

def binom_test(n, k, p):
    return sum(binom_pmf(n, i, p) for i in range(k, n + 1))

p_value = binom_test(n, m, p0)
print(f"p-value: {p_value:.5f}")
