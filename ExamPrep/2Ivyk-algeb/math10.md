10. Įvykiai A, B, C yra poromis nesutaikomi, P (A) = 1/3, P (B) = 1/4, P (C) = 1/5. Suraskite
### Tikimybė P((A ∪ B) ∩ C)

Norėdami apskaičiuoti tikimybę \(P((A \cup B) \cap C)\), pirmiausia išnagrinėkime sąlygas ir panaudokime tikimybių savybes.

#### Duota:
- Įvykiai \(A\), \(B\), \(C\) yra poromis nesutaikomi (t. y. \(A \cap B = \emptyset\), \(A \cap C = \emptyset\), \(B \cap C = \emptyset\)).
- \(P(A) = \frac{1}{3}\)
- \(P(B) = \frac{1}{4}\)
- \(P(C) = \frac{1}{5}\)

Reikia rasti:
\[
P((A \cup B) \cap C)
\]

#### Sprendimas:
1. **Poromis nesutaikomų įvykių savybės**:
    - Kadangi \(A\), \(B\), \(C\) yra poromis nesutaikomi, tai \(A \cap C = \emptyset\) ir \(B \cap C = \emptyset\). Todėl:
      \[
      (A \cup B) \cap C = (A \cap C) \cup (B \cap C) = \emptyset \cup \emptyset = \emptyset
      \]
    - Tai reiškia, kad \((A \cup B) \cap C\) yra negalimas įvykis (niekada neįvyksta).

2. **Tikimybė negalimo įvykio**:
    - Bet kurio negalimo įvykio tikimybė yra 0:
      \[
      P(\emptyset) = 0
      \]

#### Galutinis rezultatas:
\[
P((A \cup B) \cap C) = P(\emptyset) = 0
\]

#### Paaiškinimas brėžiniu:
Jeigu pavaizduotume įvykius \(A\), \(B\) ir \(C\) kaip aibes Venno diagramoje, kurios nesikerta (nes yra poromis nesutaikomos), tai:
- \(A \cup B\) būtų dviejų atskirų aibių \(A\) ir \(B\) sąjunga.
- Ši sąjunga \(A \cup B\) visiškai nesikirs su \(C\), nes \(A\) ir \(C\) bei \(B\) ir \(C\) yra nesutaikomos.
- Todėl \((A \cup B) \cap C\) atitiks tuščią aibę (nesikertančią sritį).

**Atsakymas**:
\[
P((A \cup B) \cap C) = 0
\]
