import scipy.stats as stats

def calculate_cdf_max_binomial(p, q, n, a):
    # Floor of a since we're dealing with discrete variables
    k = int(a)
    
    # Calculate P(X ≤ k) where X ~ Bin(n, p)
    p_x = sum(stats.binom.pmf(i, n, p) for i in range(k+1))
    
    # Calculate P(Y ≤ k) where Y ~ Bin(n, q)
    p_y = sum(stats.binom.pmf(i, n, q) for i in range(k+1))
    
    # Return P(max(X,Y) ≤ k) = P(X ≤ k and Y ≤ k) = P(X ≤ k) * P(Y ≤ k)
    return p_x * p_y

# Given parameters
p = 0.26
q = 0.21
n = 4
a = 1.55

# Calculate and print the result
result = calculate_cdf_max_binomial(p, q, n, a)
print(f"F_Z({a}) = P(max(X,Y) ≤ {a}) = {result:.4f}")

# We can also verify by calculating probabilities directly
p_x_le_1 = stats.binom.cdf(1, n, p)
p_y_le_1 = stats.binom.cdf(1, n, q)
verification = p_x_le_1 * p_y_le_1
print(f"Verification: {verification:.4f}")