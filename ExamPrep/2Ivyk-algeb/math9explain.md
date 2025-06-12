### Sąjungos tikimybė

Sąjungos tikimybė – tai tikimybė, kad įvyks bent vienas iš dviejų (ar daugiau) įvykių.

#### 💡 Kas yra sąjungos tikimybė?

Jei du įvykiai yra \(A\) ir \(B\), tai jų sąjunga žymima kaip \(A \cup B\), ir ji reiškia:

> Įvykis „įvyko \(A\) arba \(B\) arba abu“.

**Sąjungos tikimybės formulė:**

\[
P(A \cup B) = P(A) + P(B) - P(A \cap B)
\]

Ši formulė naudojama visada, kai norime apskaičiuoti dviejų įvykių sąjungos tikimybę, nes reikia atimti sankirties tikimybę, kad jos neįskaičiuotume du kartus.

#### 📌 Kada galima naudoti sąjungos tikimybę?

Galima naudoti visada, kai norime rasti tikimybę, kad įvyks bent vienas iš kelių įvykių:

- **Nesutaikomi įvykiai:** Jei įvykiai negali įvykti kartu (\(A \cap B = \emptyset\)), tai \(P(A \cap B) = 0\), ir formulė tampa paprastesnė:

\[
P(A \cup B) = P(A) + P(B)
\]

- **Sutaikomi įvykiai:** Jei įvykiai gali įvykti kartu, reikia žinoti sankirties tikimybę \(P(A \cap B)\).

#### 🧠 Pavyzdys su trimis įvykiais

Jei turime tris įvykius \(A\), \(B\), \(C\), tai bendra sąjungos tikimybė būtų:

\[
P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)
\]

✅ **Tavo uždavinio atveju:**

Kadangi įvykiai \(A\), \(B\), \(C\) yra poromis nesutaikomi, tai:

\[
P(A \cap B) = 0, \quad P(A \cap C) = 0, \quad P(B \cap C) = 0, \quad P(A \cap B \cap C) = 0
\]

Dėl to visos sankirties reikšmės tampa 0, o bet kokių sąjungų tikimybės tiesiog susideda.

#### 🎯 Išvada:

- Sąjungos tikimybės formulė leidžia apskaičiuoti dviejų ar daugiau įvykių sąjungos tikimybę.
- Ji yra universali ir taikoma tiek nesutaikomiems, tiek sutaikomiems įvykiams, bet nesutaikomiems ji supaprastėja.