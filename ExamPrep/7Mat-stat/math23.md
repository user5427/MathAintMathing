23. Kaip remiantis CRT sudaromas kriterijus hipotez ˙ems apie proporcijas H0 : p = p0, H1 : p >
p0 su reikšmingumo lygmeniu α tikrinti?

1. **Formuluojame hipotezes**:
   - Nulinė hipotezė \( H_0: p = p_0 \)
   - Alternatyvi hipotezė \( H_1: p > p_0 \)

2. **Apskaičiuojame testinę statistiką**:
   \[
   Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0 (1 - p_0)}{n}}}
   \]
   kur:
   - \( \hat{p} \) – imties proporcija,
   - \( p_0 \) – hipotetinė proporcija,
   - \( n \) – imties dydis.

3. **Nustatome kritinę sritį**:
   - Esant reikšmingumo lygmeniui \( \alpha \), kritinė sritis yra \( Z > z_{1-\alpha} \), kur \( z_{1-\alpha} \) yra standartinio normaliojo skirstinio kvantilis.

4. **Priimame sprendimą**:
   - Jei \( Z \) patenka į kritinę sritį, atmetame \( H_0 \) ir priimame \( H_1 \).
   - Kitu atveju, nepakankamai pagrindo atmesti \( H_0 \).