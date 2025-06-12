# 6. Bandymo baigčių aibė – vienetinis skaičių tiesės intervalas [0; 1]

Intervalas [0; 1/2] priklauso nagrinėjamai atsitiktinių įvykių σ-algebrai. Kokie dar intervalo [0; 1] poaibiai būtinai priklauso šiai σ-algebrai?

---

Turime aibę Ω = [0, 1] ir σ-algebrą F, kurią sudaro visi poaibiai, kurie yra Borelio aibės ir tenkina tam tikras sąlygas. Žinome, kad intervalas [0, 1/2] priklauso šiai σ-algebrai, t.y. [0, 1/2] ∈ F.

Kadangi F yra σ-algebra, ji turi būti uždara atžvilgiu aibių komplementų ir skaičiuojamų sąjungų bei sankirtų. Todėl:

1. **Komplementas**:  
    Jei [0, 1/2] ∈ F, tai jo komplementas Ω \ [0, 1/2] = (1/2, 1] taip pat priklauso F.

2. **Sąjungos ir sankirtos**:  
    Galime formuoti kitus intervalus arba aibes, pavyzdžiui:  
    - [0, 1/2] ∪ (1/2, 1] = [0, 1] ∈ F (bet Ω visada yra σ-algebraje pagal apibrėžimą).  
    - Tuščia aibė ∅ taip pat priklauso F (kaip komplementas Ω).

---

### Būtinai priklausantys poaibiai

Klausimas yra apie būtinai priklausančius poaibius, tai reiškia, kad bet kokia σ-algebra, kurioje yra [0, 1/2], turi turėti ir šias aibes. Be jau minėtų, galime sugalvoti ir kitus derinius:

#### Kiti intervalai arba aibės:
Bet koks Borelio poaibis, kuris gali būti išreikštas per [0, 1/2] ir operacijas (komplementą, sąjungą, sankirtą), priklausys F. Pavyzdžiui:  
- [1/4, 1/2] = [0, 1/2] ∩ [1/4, 1] (jei [1/4, 1] yra F, bet to nežinome).  
- Tačiau ne visi poaibiai yra privalomi, nebent σ-algebra yra minimali, kurioje yra [0, 1/2].

---

### Minimalios σ-algebros atvejis

Jei σ-algebra yra minimali σ-algebra, generuota aibe [0, 1/2], tai ji susideda iš visų Borelio aibių, kurios yra simetriškos (uždaros) atžvilgiu [0, 1/2]. Tokiu atveju σ-algebrą sudaro keturios aibės:

1. ∅  
2. [0, 1/2]  
3. (1/2, 1]  
4. [0, 1]

---

### Galutinis atsakymas

Jei σ-algebra yra minimali, generuota aibe [0, 1/2], tai būtinai joje yra šios aibės:

- ∅ (tuščioji aibė)  
- [0, 1/2]  
- (1/2, 1] (komplementas [0, 1/2])  
- [0, 1] (visa erdvė)

Jei σ-algebra yra didesnė (pvz., visos Borelio aibės), tai joje bus ir kitos aibės, tačiau minimaliai reikalingos yra tik šios keturios.