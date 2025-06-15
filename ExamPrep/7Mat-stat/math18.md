18. Kaip sudaromas hipoteziu˛ H0 : a = a0, H1 : a , a0 apie normaliojo dydžio vidurki˛ su
reikšmingumo lygmeniu α tikrinimo kriterijus, kai dispersija žinoma?


### 18. Klausimas:

**Kaip sudaromas hipotezių tikrinimo kriterijus, kai:**

- H₀: \( \mu = \mu_0 \)
- H₁: \( \mu \ne \mu_0 \) (arba \( \mu > \mu_0 \), \( \mu < \mu_0 \))
- Tikriname normaliojo dydžio vidurkį
- Populiacijos dispersija \( \sigma^2 \) **yra žinoma**
- Naudojame reikšmingumo lygmenį \( \alpha \)

---

### **Sprendimo žingsniai:**

1. **Pasirenkame statistinį kriterijų:**  
   Naudojamas standartizuotas normalusis dydis (Z-statistika):

\[
Z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}
\]

Kur:
- \( \bar{X} \) – imties vidurkis,
- \( \mu_0 \) – hipotezėje H₀ nurodyta reikšmė,
- \( \sigma \) – žinomas populiacijos standartinis nuokrypis,
- \( n \) – imties dydis.

---

2. **Pasirenkame alternatyvinę hipotezę H₁** ir nustatome kriterijaus pobūdį:

- Jei \( H_1: \mu \ne \mu_0 \) – **dvipusis kriterijus**
- Jei \( H_1: \mu > \mu_0 \) – **dešininis vienpusis kriterijus**
- Jei \( H_1: \mu < \mu_0 \) – **kairinis vienpusis kriterijus**

---

3. **Apskaičiuojame kritines reikšmes** pagal reikšmingumo lygmenį \( \alpha \):

- Dvipusis: atmetame H₀, jei  
\[
|Z| > z_{\alpha/2}
\]
- Vienpusis: atmetame H₀, jei  
\[
Z > z_\alpha \quad \text{(kai H₁: } \mu > \mu_0\text{)}  
\]  
\[
Z < -z_\alpha \quad \text{(kai H₁: } \mu < \mu_0\text{)}
\]

---

4. **Sprendimas:**

- Apskaičiuojame Z-statistiką
- Palyginame su kritine reikšme
- **Jei patenka į atmetimo sritį**, atmetame H₀
- **Jei ne**, H₀ **neatmetama**

---

### **Pavyzdys (dvipusis):**

Tarkime:
- \( \bar{X} = 102 \), \( \mu_0 = 100 \), \( \sigma = 5 \), \( n = 25 \), \( \alpha = 0.05 \)
- Skaičiuojame:

\[
Z = \frac{102 - 100}{5 / \sqrt{25}} = \frac{2}{1} = 2
\]

- \( z_{0.025} \approx 1.96 \)

Kadangi \( |2| > 1.96 \), atmetame H₀. Studentas galimai **iš tikrųjų žino daugiau nei vidutiniškai** 🧠

---

### **Išvada:**

Hipotezių tikrinimo kriterijus remiasi **standartine normaliaja Z-statistika**, kai dispersija žinoma.  
Kritinės reikšmės priklauso nuo **hipotezės tipo** ir **pasirinkto α**.

