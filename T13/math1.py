# Prieš mėnesį prezidentą palankiai vertino P% rinkėjų. Pakartotinai apklausus n
# rinkėjų, m iš jų prezidento veiklą įvertino teigiamai. Patikrinkite hipotezę,
# kad rinkėjų, palankiai vertinančių prezidentą, dalis nepasikeitė. Pateikite
# gautąją p-reikšmę. ( P = 30 , n = 446 m = 117 )

import math
from scipy.stats import norm



P = 30
n = 446
m = 117


p0 = P / 100
p = m / n

z = (p - p0) / math.sqrt((p0 * (1 - p0)) / n)

p_value = 2 * (1 - norm.cdf(abs(z)))
print(f"p-value: {p_value:.4f}")