# 7. Tarkime, A ir B priklauso įvykių σ-algebrai A. Paaiškinkite, kodėl A\B irgi priklauso A.

## A\B = A ∩ Bᶜ

Norint suprasti, kodėl \( A \setminus B \) priklauso σ-algebrai \( A \), reikia atsižvelgti į σ-algebros apibrėžimą ir pagrindines savybes.

### σ-algebros apibrėžimas:

\( A \) yra σ-algebra aibėje \( \Omega \), jei tenkinamos šios sąlygos:

1. \( \Omega \in A \).
2. Jei \( A \in A \), tai \( A^c \in A \) (uždarymas atžvilgiu aibės papildinio).
3. Jei \( A_1, A_2, \dots \in A \), tai \( \bigcup_{i=1}^\infty A_i \in A \) (uždarymas atžvilgiu skaitinės sąjungos).

### \( A \setminus B \) priklausomybė \( A \):

1. \( A \setminus B \) gali būti išreikštas kaip \( A \cap B^c \). Tai tiesiog reiškia, kad imame visus elementus, kurie yra \( A \), bet nėra \( B \).
2. Kadangi \( B \in A \), tai iš σ-algebros savybių \( B^c \in A \).
3. σ-algebra yra uždara atžvilgiu baigtinių (ir skaitinių) sankirtų, todėl \( A \cap B^c \in A \).
4. Vadinasi, \( A \setminus B = A \cap B^c \in A \).

### Taip, \( A \setminus B = A \cap B^c \):

- \( A \setminus B \) reiškia aibę elementų, kurie yra \( A \), bet nėra \( B \).
- \( A \cap B^c \) reiškia elementus, kurie yra ir \( A \), ir \( B \) papildinyje (t.y. nėra \( B \)).
- Todėl \( A \setminus B \) ir \( A \cap B^c \) yra lygūs.

### Išvada:

Kadangi \( A \) yra σ-algebra, ji yra uždara atžvilgiu aibės papildinio ir baigtinių sankirtų, todėl \( A \setminus B = A \cap B^c \) priklauso \( A \).
