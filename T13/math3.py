from scipy.stats import chi2

# - Duota normaliojo atsitiktinio dydžio X ~ N(α; σ²) imtis -2.91; -2.72; -2.38;
# 0.93; -0.34; 2.91; 2.71; 3.24; -2.58; -3.63; -0.62; -0.92; 1.08; -1.74
# Patikrinkite hipotezę H_{0} / (sigma ^ 2) = sigma_{0} ^ 2 kai alternatyva a)
# H_{1} / (sigma ^ 2) > sigma_{0} ^ 2 b) H₁: σ² ≠ σο Pateikite gautas
# p-reikšmes. ( sigma_{0} = 2

x = [-2.91, -2.72, -2.38, 0.93, -0.34, 2.91, 2.71, 3.24, -2.58, -3.63, -0.62, -0.92, 1.08, -1.74]
sigma0 = 2

avr = sum(x) / len(x)
disp = sum((i - avr) ** 2 for i in x) / (len(x) - 1)

X = (len(x) - 1) * disp / sigma0 ** 2

# a H₁: σ² > σ₀²

p_value_a = 1 - chi2.cdf(X, len(x) - 1)
print(f"p-value for H₁: σ² > σ₀² is {p_value_a}")

# b) H₁: σ² ≠ σ₀²

p_value_b = 2 * min(chi2.cdf(X, len(x) - 1), 1 - chi2.cdf(X, len(x) - 1))
print(f"p-value for H₁: σ² ≠ σ₀² is {p_value_b}")