24. Kaip remiantis CRT sudaromas kriterijus hipotez ˙ems apie proporcijas H0 : p = p0, H1 : p <
p0 su reikšmingumo lygmeniu α tikrinti?

1. Apskaičiuojame standartizuotą statistiką:
   \[
   Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1 - p_0)}{n}}}
   \]
   čia:
   - \(\hat{p}\) yra imties proporcija,
   - \(p_0\) yra hipotetinė proporcija,
   - \(n\) yra imties dydis.

2. Nustatome kritinę sritį:
   - Jei \( H_1: p < p_0 \), kritinė sritis yra \( Z < -z_{\alpha} \), kur \( z_{\alpha} \) yra standartinio normaliojo skirstinio kvantilis, tenkinantis \( P(Z \leq -z_{\alpha}) = \alpha \).

3. Priimame sprendimą:
   - Jei \( Z \) patenka į kritinę sritį, atmetame \( H_0 \),
   - Kitu atveju, nepakankamai pagrindo atmesti \( H_0 \).