10. Paaiškinkite, kokie atsitiktiniai dydžiai pasiskirstę pagal chi-kvadratu desni su n laisves
### Atsitiktiniai dydžiai pasiskirstę pagal chi-kvadrat skirstinį su \( n \) laisvės laipsnių

#### Apibrėžimas:
Atsitiktinis dydis \( Y \) turi chi-kvadrat skirstinį su \( n \) laisvės laipsnių, jei jis išreiškiamas kaip \( n \) nepriklausomų standartinių normaliųjų dydžių kvadratų suma:
\[
Y = X_1^2 + X_2^2 + \cdots + X_n^2,
\]
kur \( X_i \sim N(0,1) \) ir visi \( X_i \) yra nepriklausomi.

#### Pagrindinės savybės:
- **Parametras:** Tik teigiami sveikieji skaičiai \( n \) (laisvės laipsniai).
- **Tikimasis vidurkis:** \( E[Y] = n \).
- **Dispersija:** \( \text{Var}(Y) = 2n \).
- **Skirstinys:** Asimetriškas (dešiniau pasvirtas), bet artėja prie normaliojo, kai \( n \) didėja.

#### Tankio funkcijos eskizas:
- **Forma:**
    - Kai \( n = 1 \): Tankis yra be galo aukštas ties \( y = 0 \) (nes \( X^2 \) visada neneigiamas).
    - Kai \( n \geq 2 \): Tankis prasideda ties \( y = 0 \), pasiekia maksimumą ir palaipsniui mažėja.
- **Grafiko pavyzdžiai:**
    - \( n = 1 \): Staigus kritimas nuo begalybės ties \( y = 0 \).
    - \( n = 2 \): Eksponentinis mažėjimas (panašus į \( \text{Exp}(1/2) \)).
    - \( n = 3, 4, \dots \): Skirstinys tampa plačiau išsibarstęs ir simetriškesnis.

#### Eskizas:
```
f(y)
    │
    │       n=1
    │       /\
    │      /  \
    │     /    \
    │    /      \
    │   /        \       n=2
    │  /          \     /
    │ /            \   /
    │/              \_/
    └───────────────────> y
    0
```
*(Kai \( n \) didėja, kreivė pasislenka į dešinę ir tampa platėja.)*

#### Praktinis taikymas:
Chi-kvadrat skirstinys naudojamas:
- Statistinėse hipotezių tikrinimuose (pvz., chi-kvadrato testas).
- Dispersijos pasikliautinuosiuose intervaluose.
- Tikimybių modeliuose, kur reikia aprašyti kvadratinių dydžių sumą.

#### Papildoma pastaba:
Jei \( Y \sim \chi^2(n) \), tai jo tankio funkcija:
\[
f_Y(y) = \frac{1}{2^{n/2} \Gamma(n/2)} y^{n/2 - 1} e^{-y/2}, \quad y > 0,
\]
kur \( \Gamma \) – gama funkcija (apibendrintas faktorialas).

[Chi-kvadrat skirstinio funkcija dokumentacijoje](https://wiki.documentfoundation.org/Documentation/Calc_Functions/CHISQ.DIST)
