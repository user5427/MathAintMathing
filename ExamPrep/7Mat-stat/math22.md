22. Kaip remiantis CRT sudaromas kriterijus hipotez ˙ems apie proporcijas H0 : p = p0, H1 : p ,
p0 su reikšmingumo lygmeniu α tikrinti?

Hipotezės apie proporciją H₀: p = p₀ tikrinimas remiantis Chi kvadrato (CRT) kriterijumi:

1. Formuluojamos hipotezės:
   - H₀: p = p₀ (nulinė hipotezė)
   - H₁: p ≠ p₀ (alternatyvioji hipotezė, dvipusis variantas)
   (Galimos ir vienpusės alternatyvos H₁: p > p₀ arba H₁: p < p₀)

2. Skaičiuojami stebimi (O) ir teoriniai (E) dažniai:
   - Pastebėta: X sėkmingų įvykių iš n bandymų
   - O₁ = X (sėkmės), O₂ = n - X (nesėkmės)
   - E₁ = n·p₀, E₂ = n·(1 - p₀)

3. Skaičiuojamas Chi kvadrato statistikos:
   χ² = Σ[(Oᵢ - Eᵢ)²/Eᵢ] = (O₁ - E₁)²/E₁ + (O₂ - E₂)²/E₂

4. Nustatomas kritinė sritis:
   - Laisvės laipsnių skaičius df = 1
   - Kritinė reikšmė χ²_crit randama iš Chi kvadrato skirstinio lentelių su df=1 ir α

5. Sprendimo taisyklė:
   - Jei χ² ≥ χ²_crit → atmesti H₀
   - Jei χ² < χ²_crit → nėra pagrindo atmesti H₀

Pastaba: Tikslesni rezultatai gaunami naudojant normalųjį aproksimavimą su pataisomis.