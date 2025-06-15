31. Užrašykite formulę sąjungos tikimybei P (X ∪ Y ∪ Z ∪ U ) reikšti. Suprastinkite formulę
Pasinaudodami tuo, kad įvykis X negali įvykti kartu su kitais įvykiais:

X nesutaikomas su Y, Z ir U, todėl:

Jei įvykis X yra nesutaikomas su Y, Z ir U (t.y., \(X \cap Y = \emptyset\), \(X \cap Z = \emptyset\), \(X \cap U = \emptyset\)), tai sąjungos tikimybė \(P(X \cup Y \cup Z \cup U)\) labai supaprastėja.

**Bendroji formulė (įtraukimo-išskirstymo principas):**

\[
P(X \cup Y \cup Z \cup U) = P(X) + P(Y) + P(Z) + P(U) - P(Y \cap Z) - P(Y \cap U) - P(Z \cap U) + P(Y \cap Z \cap U)
\]

**Supaprastinta formulė (nes X nesikerta su Y, Z, U):**

Kadangi X nesikerta su jokiais kitais įvykiais, tai:

- Visos sankirtos su X yra tuščios aibės, todėl jų tikimybės lygios 0:
    \[
    P(X \cap Y) = 0, \, P(X \cap Z) = 0, \, P(X \cap U) = 0, \, P(X \cap Y \cap Z) = 0, \, \text{ir t.t.}
    \]

- Todėl formulėje liks tik:
    - Atskiri tikimybės \(P(X)\), \(P(Y)\), \(P(Z)\), \(P(U)\),
    - Sąlygos, kurios neįtraukia X (nes jis nesikerta).

**Galutinė supaprastinta formulė:**

\[
P(X \cup Y \cup Z \cup U) = P(X) + P(Y \cup Z \cup U)
\]

Arba išskleidus \(P(Y \cup Z \cup U)\):

\[
P(X \cup Y \cup Z \cup U) = P(X) + P(Y) + P(Z) + P(U) - P(Y \cap Z) - P(Y \cap U) - P(Z \cap U) + P(Y \cap Z \cap U)
\]

**Kodėl taip paprasta?**

- X yra visiškai atskiras nuo kitų įvykių, todėl jo sąjunga su jais yra tiesiog disjunkcija.
- \(P(X \cup \text{kazkas}) = P(X) + P(\text{kazkas})\), nes X nesikerta.

**Atsakymas:**

\[
P(X \cup Y \cup Z \cup U) = P(X) + P(Y) + P(Z) + P(U) - P(Y \cap Z) - P(Y \cap U) - P(Z \cap U) + P(Y \cap Z \cap U)
\]

*(arba pirmasis variantas, jei nenorima skleisti \(P(Y \cup Z \cup U)\).)*

Gud! 😸 Jei kas neaišku – klausk!