12. Atliekami penki polinominės schemos bandymai, kiekviename bandyme galimos trys
baigtys, pirmųjų dviejų baigčių tikimybės \( p_1 = 0.2 \), \( p_2 = 0.3 \), bandymų serijoje gauti sėkmių skaičiai \( S_1, S_2, S_3 \). Apskaičiuokite tikimybę \( P(S_1 = 2, S_2 = 1) \).

\( p_3 = 1 - p_1 - p_2 = 0.5 \)

Turime penkis nepriklausomus bandymus, kiekviename iš kurių galimos trys baigtys su tikimybėmis:

- \( p_1 = 0.2 \) (pirmoji baigtis),
- \( p_2 = 0.3 \) (antroji baigtis),
- \( p_3 = 1 - p_1 - p_2 = 0.5 \) (trečioji baigtis).

Mus domina tikimybė \( P(S_1 = 2, S_2 = 1) \), kur \( S_1 \) yra pirmųjų baigčių skaičius, o \( S_2 \) – antrojo tipo baigčių skaičius per penkis bandymus.

Kadangi \( S_3 = 5 - S_1 - S_2 \), tai norima tikimybė yra polinominio skirstinio tikimybė:

\[
P(S_1 = k, S_2 = l) = \frac{n!}{k! \, l! \, (n-k-l)!} \, p_1^k \, p_2^l \, p_3^{n-k-l},
\]

kur \( n = 5 \), \( k = 2 \), \( l = 1 \), \( p_1 = 0.2 \), \( p_2 = 0.3 \), \( p_3 = 0.5 \).

Taigi,

\[
P(S_1 = 2, S_2 = 1) = \frac{5!}{2! \, 1! \, 2!} \cdot (0.2)^2 \cdot (0.3)^1 \cdot (0.5)^2.
\]

Skaičiuojame:

- Faktorialai:
    - \( 5! = 120 \),
    - \( 2! = 2 \),
    - \( 1! = 1 \),
    - \( 2! = 2 \).

\[
\frac{120}{2 \cdot 1 \cdot 2} = \frac{120}{4} = 30.
\]

- Tikimybių daugyba:
    - \( (0.2)^2 = 0.04 \),
    - \( (0.3)^1 = 0.3 \),
    - \( (0.5)^2 = 0.25 \).

\[
0.04 \cdot 0.3 \cdot 0.25 = 0.003.
\]

- Galutinis rezultatas:

\[
30 \cdot 0.003 = 0.09.
\]

Taigi, tikimybė \( P(S_1 = 2, S_2 = 1) \) yra:

\[
0.09
\]