7. Atliekama n = 5 Bernulio schemos bandymu, sekmes tikimybe viename bandyme p = 0,3.
Kokia tikimybe, kad atlikę bandymus patirsime bent dvi nesekmes?

P(Sn >= 4) = P(Sn = 4) + P(Sn = 5) = x
P(Sn < 4) = P(Sn = 0) + P(Sn = 1) + P(Sn = 2) + P(Sn = 3) = y


1 būdas: Tiesioginis skaičiavimas

Tikimybė, kad bus lygiai kk sėkmių, yra:
P(k)=C(5,k)⋅pk⋅q5−k
P(k)=C(5,k)⋅pk⋅q5−k

kur C(5,k)C(5,k) yra kombinacijų skaičius.

Apskaičiuokime kiekvieną atvejį:

    P(k=0)=C(5,0)⋅0.30⋅0.75=1⋅1⋅0.16807=0.16807P(k=0)=C(5,0)⋅0.30⋅0.75=1⋅1⋅0.16807=0.16807

    P(k=1)=C(5,1)⋅0.31⋅0.74=5⋅0.3⋅0.2401=5⋅0.07203=0.36015P(k=1)=C(5,1)⋅0.31⋅0.74=5⋅0.3⋅0.2401=5⋅0.07203=0.36015

    P(k=2)=C(5,2)⋅0.32⋅0.73=10⋅0.09⋅0.343=10⋅0.03087=0.3087P(k=2)=C(5,2)⋅0.32⋅0.73=10⋅0.09⋅0.343=10⋅0.03087=0.3087

    P(k=3)=C(5,3)⋅0.33⋅0.72=10⋅0.027⋅0.49=10⋅0.01323=0.1323P(k=3)=C(5,3)⋅0.33⋅0.72=10⋅0.027⋅0.49=10⋅0.01323=0.1323

Sudėję:
P(k≤3)=0.16807+0.36015+0.3087+0.1323=0.96922
P(k≤3)=0.16807+0.36015+0.3087+0.1323=0.96922

2 būdas: Skaičiavimas per priešingą įvykį

Priešingas įvykis yra "mažiau nei dvi nesėkmės", t.y. "4 arba 5 sėkmės" (nes jei sėkmių yra 4, tai nesėkmių 1; jei sėkmių 5, tai nesėkmių 0).

Taigi:
P(bent dvi nese˙kme˙s)=1−P(k=4)−P(k=5)
P(bent dvi nese˙kme˙s)=1−P(k=4)−P(k=5)

Apskaičiuokime:

    P(k=4)=C(5,4)⋅0.34⋅0.71=5⋅0.0081⋅0.7=5⋅0.00567=0.02835P(k=4)=C(5,4)⋅0.34⋅0.71=5⋅0.0081⋅0.7=5⋅0.00567=0.02835

    P(k=5)=C(5,5)⋅0.35⋅0.70=1⋅0.00243⋅1=0.00243P(k=5)=C(5,5)⋅0.35⋅0.70=1⋅0.00243⋅1=0.00243

Taigi:
P(bent dvi nese˙kme˙s)=1−0.02835−0.00243=1−0.03078=0.96922
P(bent dvi nese˙kme˙s)=1−0.02835−0.00243=1−0.03078=0.96922

Abu būdai duoda tą patį rezultatą.

Atsakymas:
Tikimybė, kad bus bent dvi nesėkmės, yra 0.969220.96922​.