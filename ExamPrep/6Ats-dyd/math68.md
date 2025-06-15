68. Atsitiktinio dydžio X vidurkis lygus 1, o dispersija 0. Kam lygi šio dydžio pasiskirstymo
funkcijos reikšmė FX(1.5)?

Norėdami rasti atsitiktinio dydžio \( X \) pasiskirstymo funkcijos reikšmę \( F_X(1.5) \), turime atsižvelgti į pateiktą informaciją apie \( X \):

- **Vidurkis (matematinė viltis):** \( E[X] = 1 \)
- **Dispersija:** \( \text{Var}(X) = 0 \)

### Dispersijos reikšmė:

Dispersija \( \text{Var}(X) = 0 \) rodo, kad atsitiktinis dydis \( X \) yra nekintantis (deterministinis). Tai reiškia, kad \( X \) su tikimybe 1 įgyja reikšmę, lygią savo vidurkiui:
\[
X = 1 \quad (\text{beveik visur})
\]

### Pasiskirstymo funkcija \( F_X(x) \):

Pasiskirstymo funkcija \( F_X(x) \) apibrėžiama kaip:
\[
F_X(x) = P(X \leq x)
\]

Kadangi \( X \) visada lygus 1, turime:

- Jei \( x < 1 \), \( P(X \leq x) = 0 \), nes \( X \) niekada nebus mažesnis už 1.
- Jei \( x \geq 1 \), \( P(X \leq x) = 1 \), nes \( X \) visada yra 1, o \( 1 \leq x \).

Todėl pasiskirstymo funkcija yra:
\[
F_X(x) =
\begin{cases} 
0, & \text{jei } x < 1, \\
1, & \text{jei } x \geq 1.
\end{cases}
\]

### Reikšmė \( F_X(1.5) \):

Kadangi \( 1.5 \geq 1 \), tai:
\[
F_X(1.5) = 1
\]

### Galutinis atsakymas:
\[
1
\]