29. Tegu Ai , i = 1, 2, . . . , 6 yra bet kokie atsitiktiniai ivykiai, A - visu šiu ivykiu sąjunga.
Prisiminkime formulę P (A) = S1 − S2 + S3 − S4 + S5 − S6. Kokie demenys sudaro sumą S3 ir kiek tu
demenu yra?
Tai yra įtraukimo-išskirstymo principo (angl. inclusion-exclusion principle) atvejis, kai turime 6 atsitiktinius įvykius \( A_1, A_2, \dots, A_6 \), o \( A = \bigcup_{i=1}^6 A_i \).

Formulė:
\[
P(A) = S_1 - S_2 + S_3 - S_4 + S_5 - S_6,
\]

kur:

- \( S_k \) yra visų \( k \)-eilių sankirtų tikimybių suma.

### Kas sudaro \( S_3 \)?

\( S_3 \) apima visus galimus 3 skirtingų įvykių sankirtų tikimybių dėmenis:
\[
S_3 = \sum_{1 \leq i < j < k \leq 6} P(A_i \cap A_j \cap A_k).
\]

### Kiek tokių dėmenų yra?

Kadangi renkamės 3 įvykius iš 6, tai dėmenų skaičius yra kombinacijų skaičius:
\[
\binom{6}{3} = 20.
\]

### Atsakymas:

- \( S_3 \) sudaro visos galimos 3 įvykių sankirtos \( P(A_i \cap A_j \cap A_k) \).
- Dėmenų skaičius: 20.

### Pavyzdys:

Jei turime \( A_1, A_2, A_3, A_4, A_5, A_6 \), tai \( S_3 \) apims:
\[
P(A_1 \cap A_2 \cap A_3), P(A_1 \cap A_2 \cap A_4), \dots, P(A_4 \cap A_5 \cap A_6).
\]

(Iš viso 20 kombinacijų).
