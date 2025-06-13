2. Atliekama n (n ⩾ 5) Bernulio schemos bandymų. Kiek palankių baigčių turi įvykis
### Įvykis A: Patirtos 4 nesėkmės

Norint nustatyti, kiek palankių baigčių turi įvykis \( A = \{ \text{patirtos 4 nesėkmės} \} \) atliekant \( n \) (\( n \geq 5 \)) Bernulio bandymų, reikia suprasti, kad:

1. **Bernulio bandymai**: Kiekvienas bandymas turi dvi galimas baigtis – sėkmę (pvz., \( S \)) arba nesėkmę (pvz., \( F \)).

2. **Įvykis \( A \)**: Tai reiškia, kad per \( n \) bandymų lygiai 4 kartus įvyko nesėkmė (\( F \)). Likusiuose \( n - 4 \) bandymuose turi būti sėkmės (\( S \)).

3. **Palankios baigtys**: Tai visos galimos sekos, kuriose yra 4 nesėkmės ir \( n - 4 \) sėkmės. Tokių sekų skaičius yra lygus kombinacijų skaičiui, t.y., keliais būdais galime iš \( n \) bandymų pasirinkti 4, kurie bus nesėkmės (arba \( n - 4 \), kurie bus sėkmės).

4. **Kombinacijos formulė**:
    \[
    C(n, 4) = \binom{n}{4}
    \]
    arba ekvivalentiškai:
    \[
    C(n, n - 4) = \binom{n}{n - 4}
    \]

    Kadangi \( \binom{n}{k} = \binom{n}{n - k} \), tai:
    \[
    C(n, 4) = C(n, n - 4)
    \]

### Palankių baigčių skaičius:
\[
C(n, n - 4)
\]