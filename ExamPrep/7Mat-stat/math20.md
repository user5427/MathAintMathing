20. Kaip sudaromas hipoteziu˛ H0 : a = a0, H1 : a > a0 apie normaliojo dydžio vidurki˛ su
reikšmingumo lygmeniu α tikrinimo kriterijus, kai dispersija žinoma?

### 20. Klausimas:

**Kaip sudaromas hipotezių tikrinimo kriterijus, kai:**

- H₀: \( \mu = \mu_0 \)
- H₁: \( \mu > \mu_0 \)  ⟶ **vienpusė dešininė alternatyva**
- Dispersija \( \sigma^2 \) **yra žinoma**
- Tikriname normaliojo dydžio vidurkį
- Naudojamas reikšmingumo lygmuo \( \alpha \)

---

### **Statistika:**

Kadangi žinoma populiacijos dispersija, naudojama **Z-statistika**:

\[
Z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}
\]

Kur:
- \( \bar{X} \) – imties vidurkis
- \( \mu_0 \) – hipotezės reikšmė
- \( \sigma \) – žinomas populiacijos standartinis nuokrypis
- \( n \) – imties dydis

---

### **Kritinė sritis (kai H₁: \( \mu > \mu_0 \)):**

Kadangi alternatyva yra **vienpusė**, H₀ atmetama, kai:

\[
Z > z_\alpha
\]

Kur \( z_\alpha \) – **kritinė reikšmė** iš standartinio normaliojo paskirstymo, tokia, kad:

\[
P(Z > z_\alpha) = \alpha
\]

---

### **Sprendimo eiga:**

1. Apskaičiuojame Z-statistiką
2. Surandame \( z_\alpha \) (pvz., jei \( \alpha = 0.05 \), tai \( z_{0.05} \approx 1.645 \))
3. Jei \( Z > z_\alpha \), **atmetame H₀**
4. Jei \( Z \leq z_\alpha \), H₀ **neatmetama**

---

### **Pavyzdys:**

Tarkime:
- \( \bar{X} = 105 \)
- \( \mu_0 = 100 \)
- \( \sigma = 10 \)
- \( n = 25 \)
- \( \alpha = 0.05 \)

Skaičiuojame:

\[
Z = \frac{105 - 100}{10 / \sqrt{25}} = \frac{5}{2} = 2.5
\]

Kritinė reikšmė: \( z_{0.05} \approx 1.645 \)

Kadangi \( 2.5 > 1.645 \), **atmetame H₀** ⟶ statistiškai pagrįsta manyti, kad \( \mu > \mu_0 \)

---

### **Išvada:**

Kai tikriname hipotezę \( H_0: \mu = \mu_0 \) prieš \( H_1: \mu > \mu_0 \) su **žinoma dispersija**,  
naudojame **vienpusį Z-testą**, o H₀ atmetama, jei Z-statistika viršija kritinę ribą \( z_\alpha \).
