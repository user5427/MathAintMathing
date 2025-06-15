o funkcijos reikšmė \( F_X(1) \)?

Duota:

- Vidurkis (matematinė vilties reikšmė): \( E[X] = 2 \)
- Dispersija: \( \text{Var}(X) = 0 \)

**Dispersija lygi 0:**

Kai atsitiktinio dydžio \( X \) dispersija yra 0, tai reiškia, kad \( X \) yra nekintantis dydis (deterministinis). Todėl \( X \) su tikimybe 1 (t.y. beveik visada) įgyja reikšmę, lygią savo vidurkiui:
\( X = 2 \) (beveik visur)

**Pasiskirstymo funkcija \( F_X(x) \):**

Pasiskirstymo funkcija apibrėžiama kaip:
\[ F_X(x) = P(X \leq x) \]

Kadangi \( X \) visada lygus 2, tai:

- Jei \( x < 2 \), \( P(X \leq x) = 0 \), nes \( X \) niekada nėra mažesnis už 2.
- Jei \( x \geq 2 \), \( P(X \leq x) = 1 \), nes \( X \) visada tenkina \( 2 \leq x \).

Todėl:
\[
F_X(x) =
\begin{cases} 
0, & \text{jei } x < 2 \\
1, & \text{jei } x \geq 2 
\end{cases}
\]

**Reikšmė \( F_X(1) \):**

Kadangi \( 1 < 2 \), tai:
\[ F_X(1) = 0 \]

**Atsakymas:** \( 0 \)