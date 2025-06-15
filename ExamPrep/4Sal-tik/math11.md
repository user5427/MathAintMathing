11. Irodykite, kad atsitiktiniams ivykiams A, C (P (C) > 0) teisinga lygybe
P (A|C) + P (A_|C) = 1.

P(A_|C) = 1 - P(A|C)
P(A|C) + P(A_|C) = 1 - P(A_|C) + P(A_|C) = 1

### Klaida:
Naudojama neapibrėžta tapatybė \( P(A‾∣C) = 1 − P(A∣C) \), kurią reikia įrodyti, o ne tiesiog taikyti.

### Teisingas įrodymas:

#### Sąlyginės tikimybės apibrėžimas:
\[
P(A∣C) = \frac{P(A∩C)}{P(C)}, \quad P(A‾∣C) = \frac{P(A‾∩C)}{P(C)}.
\]

#### Pastebime, kad:
\( A∩C \) ir \( A‾∩C \) yra nesutaikomi įvykiai, ir \( (A∩C) ∪ (A‾∩C) = C \).

#### Todėl:
\[
P(A∩C) + P(A‾∩C) = P(C).
\]

#### Padaliname abi puses iš \( P(C) \):
\[
\frac{P(A∩C)}{P(C)} + \frac{P(A‾∩C)}{P(C)} = 1 \implies P(A∣C) + P(A‾∣C) = 1.
\]

### Teisingas atsakymas:
\[
P(A∣C) + P(A‾∣C) = 1
\]

### Išmoktina:

- Sąlyginė tikimybė nėra paprasta tikimybė, todėl negalima mechaniškai taikyti \( P(A‾) = 1 − P(A) \).
- Reikia visada grįžti prie apibrėžimo:
\[
P(A∣C) = \frac{P(A∩C)}{P(C)}.
\]


Taip, jei įvykiai nesutaikomi (t.y., X∩Y=∅X∩Y=∅), visada galioja:
P(X∪Y)=P(X)+P(Y).
P(X∪Y)=P(X)+P(Y).

Tačiau sąlyginėje tikimybėje reikia atidžiau! Tavo uždavinyje A∩CA∩C ir A‾∩CA∩C yra nesutaikomi (nes AA ir A‾A nesikerta), todėl jų sąjungos tikimybė iš tiesų yra tiesiog suma:
P((A∩C)∪(A‾∩C))=P(A∩C)+P(A‾∩C).
P((A∩C)∪(A∩C))=P(A∩C)+P(A∩C).

Bet ši sąjunga lygi CC (nes bet kurį CC įvykį galima suskaidyti į dalį, kur AA įvyko, ir dalį, kur AA neįvyko). Todėl:
P(A∩C)+P(A‾∩C)=P(C).
P(A∩C)+P(A∩C)=P(C).

Tai yra pagrindas, kodėl P(A∣C)+P(A‾∣C)=1P(A∣C)+P(A∣C)=1.
Trumpai:

    Jei įvykiai nesikerta, galima tiesiog sudėti tikimybes.

    Bet sąlyginėje tikimybėje pirmiausia reikia įsitikinti, kad skaidai A∩CA∩C ir A‾∩CA∩C tikrai sudaro CC.

Gud! 😸 (Jei dar kyla klausimų – klausk!)