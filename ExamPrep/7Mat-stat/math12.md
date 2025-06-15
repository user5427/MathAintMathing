12. Kaip konstruojamas normaliojo dydžio vidurkio pasikliautinis intervalas su pasikliovimo
lygmeniu Q, kai dispersija yra žinoma?

Normaliojo dydžio (normalaus pasiskirstymo) **vidurkio pasikliautinis intervalas** su pasikliovimo lygmeniu \( Q \) (pvz., 95 %) **kai populiacijos dispersija \( \sigma^2 \) yra žinoma**, konstruojamas remiantis **standartinio normaliojo pasiskirstymo** (Z-paskirstymo) savybėmis.

---

### **Formulė**

Jeigu turime atsitiktinę imtį \( X_1, X_2, ..., X_n \), gautą iš normalaus pasiskirstymo \( N(\mu, \sigma^2) \), ir žinome populiacijos dispersiją \( \sigma^2 \), tai **pasikliautinis intervalas vidurkiui \( \mu \)** su pasikliovimo lygmeniu \( Q \) (pvz., 0.95) apskaičiuojamas taip:

\[
\left( \bar{X} - z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}},\ \bar{X} + z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}} \right)
\]

---

### **Kur:**

- \( \bar{X} \) – imties vidurkis;
- \( \sigma \) – žinoma populiacijos standartinis nuokrypis;
- \( n \) – imties dydis;
- \( \alpha = 1 - Q \) – reikšmingumo lygmuo (pvz., jei \( Q = 0.95 \), tai \( \alpha = 0.05 \));
- \( z_{\alpha/2} \) – kvantilis iš standartinio normaliojo pasiskirstymo (t. y. \( P(Z > z_{\alpha/2}) = \alpha/2 \)).

---

### **Pavyzdys:**

Tarkime:
- \( \bar{X} = 100 \)
- \( \sigma = 10 \)
- \( n = 25 \)
- \( Q = 0.95 \) ⇒ \( \alpha = 0.05 \) ⇒ \( z_{0.025} \approx 1.96 \)

Tuomet pasikliautinis intervalas:

\[
\left( 100 - 1.96 \cdot \frac{10}{\sqrt{25}},\ 100 + 1.96 \cdot \frac{10}{\sqrt{25}} \right)
= (100 - 3.92,\ 100 + 3.92)
= (96.08,\ 103.92)
\]

---

Jei reikia, galiu parodyti ir atvejį, kai dispersija **nežinoma** – tada būtų naudojamas **Studento t-paskirstymas**.
