24. Paprastasis atsitiktinis dydis igyja tris didesnes už 1 reikšmes. Irodykite, kad dydžio
vidurkis irgi yra didesnis už 1.

#
# P(X = x1) = p1
# P(X = x2) = p2
# P(X = x3) = p3

# E(X) = x1 * p1 + x2 * p2 + x3 * p3
# P(X = x1) + P(X = x2) + P(X = x3) = 1

xi*pi = pi + (xi - 1) * pi
# E(X) = p1 + (x1 - 1) * p1 + p2 + (x2 - 1) * p2 + p3 + (x3 - 1) * p3
# E(X) = 1 + (x1 - 1) * p1 + (x2 - 1) * p2 + (x3 - 1) * p3
(x1 - 1) * p1 + (x2 - 1) * p2 + (x3 - 1) * p3 > 0
# Kadangi x1, x2, x3 yra didesni už 1, tai (x1 - 1), (x2 - 1), (x3 - 1) yra didesni už 0.
Vadinasi E(X) > 1.

2) Trumpesnis įrodymas:

Kadangi visos reikšmės xi>1xi​>1, o tikimybės pipi​ yra teigiamos ir sudaro 1, tai:
E(X)=x1⋅p1+x2⋅p2+x3⋅p3>1⋅p1+1⋅p2+1⋅p3=p1+p2+p3=1.

Taigi, E(X)>1E(X)>1.