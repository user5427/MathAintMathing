18. Optimalaus pasirinkimo uždavinyje objektų skaičius n = 5. Rinkimosi strategijos parametras m = 2. Kokia tikimybė likti be nieko, t.y., nieko nepasirinkti?

Norėdami apskaičiuoti tikimybę likti be nieko (t. y., nieko nepasirinkti) optimalaus pasirinkimo uždavinyje, kai objektų skaičius \(n = 5\) ir rinkimosi strategijos parametras \(m = 2\), galime naudoti šį samprotavimą:

### Optimalaus pasirinkimo problema (Secretary Problem)

1. Turime \(n\) kandidatų (arba objektų), išdėstytų atsitiktine tvarka.
2. Peržiūrime juos vieną po kito ir turime nuspręsti, kurį pasirinkti.
3. **Strategija**: praleidžiame pirmus \(m\) kandidatų, o tada pasirenkame pirmąjį, kuris yra geresnis už visus ankstesnius.
4. Jei toks kandidatas nepasirodo, esame priversti pasirinkti paskutinįjį.

### Tikimybė nieko nepasirinkti

Tikimybė likti be nieko atitinka tikimybę, kad geriausias kandidatas yra tarp pirmųjų \(m\), todėl jis bus praleistas, o vėliau neatsiras joks kandidatas, geresnis už visus ankstesnius (t. y., antras geriausias yra tarp pirmųjų \(m\), o geriausias – tarp likusių \(n - m\)).

Tačiau paprasčiau galima apskaičiuoti tikimybę, kad geriausias kandidatas yra tarp pirmųjų \(m\), nes tada jį praleisime ir nieko nepasirinksime (nes vėliau niekas nebus geresnis už jį).

Tikimybė, kad geriausias kandidatas yra tarp pirmųjų \(m\), yra:

\[
P(\text{geriausias tarp pirmų } m) = \frac{m}{n}
\]

Todėl:

\[
P(\text{nieko nepasirinkti}) = \frac{m}{n} = \frac{2}{5} = 0.4 \, (\text{arba } 40\%)
\]

### Patikrinimas

Kai \(n = 5\) ir \(m = 2\):

1. Geriausias kandidatas gali būti bet kurioje iš 5 pozicijų su vienoda tikimybe \(\frac{1}{5}\).
2. Jei geriausias yra 1-oje arba 2-oje pozicijoje (t. y., tarp pirmųjų \(m = 2\)), jį praleisime ir nieko nepasirinksime.
3. Taigi tikimybė, kad geriausias yra 1 arba 2, yra \(\frac{2}{5}\).

### Galutinis atsakymas

\[
P(\text{nieko nepasirinkti}) = \frac{2}{5} = 0.4 \, (\text{arba } 40\%)
\]
