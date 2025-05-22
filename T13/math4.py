# Buvo matuojama, kokiu greičiu (km/val) skraido žvirbliai. Padarę prielaidą,
# kad žvirblių greitis yra pagal normalųjį dėsnį pasiskirstęs atsitiktinis dydis
# X ~N(a; o²) ir naudodamiesi imties x duomenimis, patikrinkite hipotezę apie
# vidutinį greitį Ho a=a_{0}, su alternatyva H₁ a < a_{0}. Pateikite gautąją p-reikšmę.
# a_{0} = 46.5 x = [47.2, 47.2, 45.7, 45.3, 48.7, 48.2, 44.9, 46.8, 45.8, 44.2,
# 48.8, 45.6, 48.3, 48.5, 46.9, 48.7, 44.6, 45.8]

from scipy.stats import t

a0 = 46.5
x = [47.2, 47.2, 45.7, 45.3, 48.7, 48.2, 44.9, 
     46.8, 45.8, 44.2, 48.8, 45.6, 48.3, 48.5, 
     46.9, 48.7, 44.6, 45.8]

avr = sum(x) / len(x)
disp = sum((i - avr) ** 2 for i in x) / (len(x) - 1)
myT = (avr - a0) / (disp ** 0.5 / len(x) ** 0.5)

Pr = t.cdf(myT, len(x) - 1)

print(f"p-value for H₁: a < a₀ is {Pr}")