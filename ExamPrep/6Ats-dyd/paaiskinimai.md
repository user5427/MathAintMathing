9. Atsitiktinis dydis ξ pasiskirstęs pagal binomini˛ desni: ξ ∼ B(5; 0,3). Apskaičiuokite pa-
siskirstymo funkcijos reikšmę Fξ (1,5).


Fξ (1,5) priklauso intervalui [1; 2), NE (1; 2], todel skaiciuojame tik iki 2, neiskaitant 2.
Fξ(1,5) = P(ξ < 2) = P(ξ = 0) + P(ξ = 1)

---
P(X = m) = C(m + n - 1, m) * p^n * q^m
vadinsime Paskalio atsitiktiniu dydžiu ir žymėsime X ∼ B−(n, p).

---
Muavro ir Laplaso theorem:
23 teorema. Tegu p yra sėkmės tikimybė viename Bernulio schemos ban-
dyme, n bandymų skaičius, Sn – sėkmių skaičius, gautas atlikus n bandymų,
a < b – bet kokie skaičiai. Jeigu p nesikeičia, o n neaprėžtai auga, tai
P(a < (Sn - np) / √(npq) < b) → Φ(b) - Φ(a), kur Φ yra standartinio
normaliojo pasiskirstymo funkcija.


---
28 apibrėžimas. Tegu atsitiktinis dydis X yra tolydusis, 0 < α < 1.
Dydžio X α lygio kvantiliu vadinsime mažiausiąjį lygties
F_X (x) = α
sprendinį; jį žymėsime u_α. Dydį u_α taip pat vadinsime 1 − α lygio kritine
reikšme.

---
Sąlyginiu X vidurkiu su sąlyga H vadinsime skaičių
E[X|H] = ∑ x · P (X = x|H).

---
D[X] = E[(X − E[X])2]

---

Dydį σ(X) = √D[X] vadinsime atsitiktinio dydžio X standartiniu nuokrypiu

---

1. jeigu atsitiktinis dydis X turi dispersiją, ji neneigiama: D[X] > 0;
D[X] = 0 tada ir tik tada, kai dydis X yra išsigimęs;
2. teisinga lygybė D[X] = E[X^2] − E[X]^2;
3. jei c yra skaičius, tai D[cX] = c^2D[X];
4. jeigu nepriklausomi atsitiktiniai dydžiai X, Y turi dispersijas, tai ir jų
suma turi dispersiją ir D[X + Y ] = D[X] + D[Y ].

---

Normaliojo skirstinio tankio funkcija \(p(x)\) yra simetriška vidurkiui \(\mu\), o
jos maksimumas yra būtent \(x = \mu\) (šiuo atveju \(\mu = 1\)).

Kai \(\sigma^2 = 2\) (ir \(\sigma = \sqrt{2}\)), tankio funkcijos reikšmės taškuose \(x = 0\) ir \(x = 2\) yra
lygios, nes šie taškai yra simetriški vidurkiui \(x = 1\):

---

Cebisovo nelygybė teigia, kad kiek gali nukrypti atsitiktinis dydis nuo savo vidurkio ir kiek tai yra susiję su jo dispersija. 

Formule:
\[
P(|X - E[X]| \geq k) \leq \frac{D[X]}{k^2}
\]

---

Didžiųjų skaičių dėsnis
41 teorema. Tegu X1, X2, X3, . . . yra nepriklausomi atsitiktiniai dydžiai,
turintys tą patį vidurkį E[Xj ] = a ir tą pačią dispersiją. Tada kiekvienam
\[
\lim_{n \to \infty} \frac{1}{n} \sum_{j=1}^n X_j = a
\]