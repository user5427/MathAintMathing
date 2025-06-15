9. Paaiškinkite, kas yra su atsitiktiniu dydžiu X susijusio nežinomo parametro θ pasikliautinis
intervalas su pasikliovimo lygmeniu Q.

### Pasikliautinis intervalas su pasikliovimo lygmeniu Q

#### Pasikliautinis intervalas (Confidence Interval)

Pasikliautinis intervalas – tai du skaičiai (apatinė ir viršutinė riba), kurie su tam tikru pasikliovimo lygmeniu \( Q \) (pvz., 95%) nurodo, kokiame intervale tikėtinai yra nežinomas parametras \( \theta \).

#### Pagrindinės sąvokos:

- **Parametras \( \theta \)** – nežinoma reikšmė, kurią norime įvertinti (pvz., vidurkis \( \mu \), dispersija \( \sigma^2 \), regresijos koeficientas ir kt.).
- **Pasikliovimo lygmuo \( Q \)** – tikimybė (dažniausiai 90%, 95%, 99%), kad pasikliautiname intervale yra \( \theta \).
    - Pvz., \( Q = 95\% \) reiškia: "Jei imtį paimtume 100 kartų, maždaug 95 intervalai apimtų tikrąją \( \theta \) reikšmę."
- **Pasikliautino intervalo ribos** – apskaičiuojamos naudojant imties duomenis ir statistinį skirstinį (pvz., normalųjį, t-skirstinį).

#### Kaip jis susijęs su atsitiktiniu dydžiu \( X \)?

- \( X \) yra atsitiktinis dydis (pvz., matavimų rezultatai), o \( \theta \) – jo parametras (pvz., \( E[X] = \mu \)).
- Remdamiesi \( X \) imtimi, statistiškai įvertiname \( \theta \) ir nustatome, kokiame intervale jis gali būti.

#### Formalus apibrėžimas:

Pasikliautinis intervalas \([L, U]\) tenkina:
\[
P(L \leq \theta \leq U) = Q
\]
(Tikimybė, kad \( \theta \) yra tarp \( L \) ir \( U \), lygi \( Q \).)

#### Pavyzdys (vidurkio \( \mu \) pasikliautinis intervalas):

Jei \( X \sim N(\mu, \sigma^2) \) ir \( \sigma \) žinomas, 95% pasikliautinis intervalas yra:
\[
\bar{X} \pm 1.96 \cdot \frac{\sigma}{\sqrt{n}}
\]
(Čia \( \bar{X} \) – imties vidurkis, \( n \) – imties dydis.)

#### Kodėl tai svarbu?

Vietoj vieno taškinio įverčio (pvz., \( \bar{X} = 5 \)) gauname tikėtiną reikšmių rėžį (pvz., \([4.2, 5.8]\)), kuris atspindi matavimo neapibrėžtumą.

#### Trumpai:

Pasikliautinis intervalas yra "tikėtinos \( \theta \) reikšmės" su pasikliovimo tikimybe \( Q \).  
Jei \( Q = 95\% \), tai reiškia, kad 95% tokių intervalų teisingai apims \( \theta \) (bet 5% – ne).
