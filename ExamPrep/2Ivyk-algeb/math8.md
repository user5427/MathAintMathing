8. Ar toks teiginys gali buti teisingas: „A ir B yra nesutaikomi ivykiai, P (A) = 2/3, P (B) = 1/2“?
### Kodėl?

Norint patikrinti, ar teiginys gali būti teisingas, turime įsitikinti, ar tenkinamos visos tikimybių aksiomos ir sąlygos, ypač kai A ir B yra nesutaikomi įvykiai.

#### Duota:

- A ir B yra nesutaikomi įvykiai, tai reiškia, kad \( A \cap B = \emptyset \) ir \( P(A \cap B) = 0 \).
- \( P(A) = \frac{2}{3} \)
- \( P(B) = \frac{1}{2} \)

#### Tikriname, ar galioja tikimybių aksiomos:

1. **Bet kurio įvykio tikimybė yra tarp 0 ir 1:**  
    \( 0 \leq P(A) \leq 1 \) ir \( 0 \leq P(B) \leq 1 \).  
    Ši sąlyga tenkinama, nes \( \frac{2}{3} \) ir \( \frac{1}{2} \) yra tarp 0 ir 1.

2. **Visos erdvės tikimybė yra 1:**  
    \( P(\Omega) = 1 \).

3. **Nesutaikomų įvykių sąjungos tikimybė yra lygi jų tikimybių sumai:**  
    \( P(A \cup B) = P(A) + P(B) \).

#### Skaičiuojame \( P(A \cup B) \):
\[
P(A \cup B) = P(A) + P(B) = \frac{2}{3} + \frac{1}{2} = \frac{4}{6} + \frac{3}{6} = \frac{7}{6} \approx 1.1667
\]

Tačiau tikimybė negali būti didesnė už 1, nes \( P(\Omega) = 1 \), o \( A \cup B \subseteq \Omega \). Todėl \( P(A \cup B) \leq 1 \). Čia gauname prieštaravimą, nes \( \frac{7}{6} > 1 \).

#### Išvada:
Teiginys negali būti teisingas, nes nesutaikomų įvykių \( A \) ir \( B \) tikimybių suma viršija 1, kas pažeidžia tikimybių teorijos aksiomas.