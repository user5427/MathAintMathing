21. Kaip sudaromas hipoteziu˛ H0 : a = a0, H1 : a > a0 apie normaliojo dydžio vidurki˛ su
reikšmingumo lygmeniu α tikrinimo kriterijus, kai dispersija nežinoma?

### 21. Klausimas:

**Kaip sudaromas hipotezių tikrinimo kriterijus, kai:**

- H₀: \( \mu = \mu_0 \)
- H₁: \( \mu > \mu_0 \)  ⟶ vienpusė dešininė alternatyva
- Dispersija **nežinoma**
- Tikriname normaliojo dydžio vidurkį
- Reikšmingumo lygmuo: \( \alpha \)

---

### **Statistika (kai dispersija nežinoma):**

Naudojama **Studento t-statistika**:

\[
T = \frac{\bar{X} - \mu_0}{S / \sqrt{n}}
\]

Kur:
- \( \bar{X} \) – imties vidurkis
- \( \mu_0 \) – hipotezėje nurodyta reikšmė
- \( S \) – imties standartinis nuokrypis (apskaičiuojamas iš duomenų)
- \( n \) – imties dydis
- \( T \) turi **t-paskirstymą su \( n - 1 \) laisvės laipsniais**

---

### **Kritinė sritis (kai H₁: \( \mu > \mu_0 \)):**

Atmetimo taisyklė:

\[
T > t_{\alpha,\, n - 1}
\]

Kur:
- \( t_{\alpha,\, n - 1} \) – t-paskirstymo kvantilis su \( n - 1 \) laisvės laipsniais
- Kritinė reikšmė parenkama taip, kad:
  \[
  P(T > t_{\alpha,\, n - 1}) = \alpha
  \]

---

### **Sprendimo eiga:**

1. Apskaičiuojame \( \bar{X} \), \( S \), ir \( T \)
2. Nustatome kritinę t-reikšmę iš lentelės ar skaičiuotuvo
3. Jei \( T > t_{\alpha,\, n-1} \), **atmetame H₀**
4. Jei \( T \leq t_{\alpha,\, n-1} \), H₀ **neatmetama**

---

### **Pavyzdys:**

Tarkime:
- \( \bar{X} = 106 \)
- \( \mu_0 = 100 \)
- \( S = 8 \)
- \( n = 16 \)
- \( \alpha = 0.05 \)

Skaičiuojame:

\[
T = \frac{106 - 100}{8 / \sqrt{16}} = \frac{6}{2} = 3
\]

Kritinė reikšmė: \( t_{0.05,\, 15} \approx 1.753 \)

Kadangi \( 3 > 1.753 \), **atmetame H₀** ⟶ yra statistinių įrodymų, kad \( \mu > \mu_0 \)

---

### **Išvada:**

Kai dispersija nežinoma, tikrinant \( H_0: \mu = \mu_0 \) prieš \( H_1: \mu > \mu_0 \),  
naudojamas **vienpusis t-kriterijus**, o H₀ atmetama, jei apskaičiuota t-statistika viršija kritinę reikšmę \( t_{\alpha,\, n - 1} \).

