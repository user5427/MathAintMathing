90. Atsitiktiniai dydžiai X1, X2, . . . yra nepriklausomi ir vienodai pasiskirstę. Visi jie igyja tik
dvi reikšmes:
P (Xi = 0) = p, P (Xi = 1) = 1 − p, 0 < p < 1.
Suformuluokite šiems dydžiams centrinę ribinę teoremą (formuluoteje irašykite apskaičiuotas
vidurkio ir dispersijos reikšmes).

E[X] = 0 * p + 1 * (1 - p) = 1 - p
D[X] = E[X^2] - (E[X])^2 = (1-p) - (1 - p)^2 = (1 - p) - (1 - 2p + p^2) = p - p^2 = p(1 - p)
Centrinė ribinė teorema sako, kad jei turime didelį skaičių nepriklausomų ir vienodai pasiskirstusių atsitiktinių dydžių, tai jų suma (arba vidurkis) bus apytiksliai normaliai pasiskirstę su vidurkiu ir dispersija, apskaičiuotomis pagal šias formules.
Sn​=X1​+X2​+⋯+Xn
Zn = Sn - n * E[X] / sqrt(n * D[X]) = (Sn - n(1 - p)) / sqrt(n * p(1 - p))

Zn -(d)> N(0, 1)