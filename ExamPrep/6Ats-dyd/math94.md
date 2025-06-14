94. Atsitiktiniai dydžiai X1, X2, . . . yra nepriklausomi ir pasiskirstę pagal tą patį binominį desni
Xi ∼ B(10; 0,5). Suformuluokite šiems dydžiams centrinę ribinę teoremą (formuluoteje irašykite
apskaičiuotas vidurkio ir dispersijos reikšmes).

E[X] = n * p = 10 * 0.5 = 5
D[X] = n * p * (1 - p) = 10 * 0.5 * (1 - 0.5) = 10 * 0.5 * 0.5 = 2.5
Centrinė ribinė teorema sako, kad jei turime didelį skaičių nepriklausomų ir vienodai pasiskirstusių atsitiktinių dydžių, tai jų suma (arba vidurkis) bus apytiksliai normaliai pasiskirstę su vidurkiu ir dispersija, apskaičiuotomis pagal šias formules.
Sn = X1 + X2 + ... + Xn
Zn = (Sn - n * E[X]) / sqrt(n * D[X]) = (Sn - 5n) / sqrt(2.5n)
Zn -(d)> N(0, 1)