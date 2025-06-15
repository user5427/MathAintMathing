19. Kaip sudaromas hipoteziu˛ H0 : a = a0, H1 : a , a0 apie normaliojo dydžio vidurki˛ su
reikšmingumo lygmeniu α tikrinimo kriterijus, kai dispersija nežinoma?

### 19. Klausimas:

**Kaip sudaromas hipotezių tikrinimo kriterijus, kai:**

- H₀: \( \mu = \mu_0 \)
- H₁: \( \mu \ne \mu_0 \) (arba \( \mu > \mu_0 \), \( \mu < \mu_0 \))
- Tikriname normaliojo dydžio vidurkį
- **Dispersija \( \sigma^2 \) yra nežinoma**
- Naudojame reikšmingumo lygmenį \( \alpha \)

---

### **Sprendimo žingsniai:**

Kai dispersija nežinoma, **vietoje Z-statistikos naudojama Studento t-statistika**, nes įverčiame dispersiją iš imties.

---

1. **Pasirenkame statistinį kriterijų:**

\[
T = \frac{\bar{X} - \mu_0}{S / \sqrt{n}}
\]

Kur:
- \( \bar{X} \) – imties vidurkis,
- \( \mu_0 \) – H₀ reikšmė,
- \( S \) – imties standartinis nuokrypis (įvertis),
- \( n \) – imties dydis,
- \( T \) pasiskirstęs pagal **Studento t-paskirstymą su \( n-1 \) laisvės laipsniu**.

---

2. **Pasirenkame alternatyvinę hipotezę H₁:**

- \( \mu \ne \mu_0 \) → **dvipusis kriterijus**
- \( \mu > \mu_0 \) → **vienpusis (dešinysis)**
- \( \mu < \mu_0 \) → **vienpusis (kairysis)**

---

3. **Nustatome kritines reikšmes:**

- Dvipusis kriterijus: atmetame H₀, jei  
\[
|T| > t_{\alpha/2,\, n-1}
\]
- Vienpusis kriterijus:
  - jei \( H_1: \mu > \mu_0 \), atmetame H₀, kai  
  \[
  T > t_{\alpha,\, n-1}
  \]
  - jei \( H_1: \mu < \mu_0 \), atmetame H₀, kai  
  \[
  T < -t_{\alpha,\, n-1}
  \]

---

4. **Sprendimas:**

- Apskaičiuojame \( T \)
- Palyginame su kritine t-reikšme
- Jei \( T \) patenka į atmetimo sritį → **atmetame H₀**
- Kitu atveju → **neatmetame H₀**

---

### **Pavyzdys (dvipusis):**

Tarkime:
- \( \bar{X} = 102 \)
- \( \mu_0 = 100 \)
- \( S = 5 \)
- \( n = 25 \)
- \( \alpha = 0.05 \) → \( t_{0.025,\, 24} \approx 2.064 \)

Skaičiuojame:

\[
T = \frac{102 - 100}{5 / \sqrt{25}} = \frac{2}{1} = 2
\]

Kadangi \( |2| < 2.064 \), H₀ **neatmetama** – nėra statistinio pagrindo teigti, kad vidurkis skiriasi nuo \( \mu_0 \).

---

### **Išvada:**

Kai dispersija nežinoma, naudojamas **Studento t-kriterijus**.  
Reikšmingumo lygmuo \( \alpha \) ir hipotezės forma lemia, kaip atrodys kritinė sritis.

