import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from fractions import Fraction

def calculate_correlation_coefficient(m, n, k1, k2):
    """
    Calculate the correlation coefficient between morning and afternoon losses
    
    Parameters:
    - m: number of 1€ coins Jonas puts in pocket
    - n: number of 2€ coins Jonas puts in pocket
    - k1: number of coins lost in the morning
    - k2: number of coins lost in the afternoon
    """
    # Total number of coins
    total_coins = m + n
    
    # Step 1: Calculate E[X1] and D(X1) - morning 1€ coin losses
    E_X1 = k1 * (m / total_coins)
    D_X1 = k1 * (m / total_coins) * ((total_coins - m) / total_coins) * ((total_coins - k1) / (total_coins - 1))
    
    # Step 2: Calculate E[X] and D(X) - morning total losses in value
    E_X = 2 * k1 - E_X1
    D_X = D_X1
    
    # Step 3: Calculate the conditional expectation E[Y1|X1]
    # After morning losses, (m - X1) coins of 1€ and (n - (k1 - X1)) = (n - k1 + X1) coins of 2€ remain
    
    # Calculating covariance and correlation using theoretical approach
    X1_values = list(range(max(0, k1 - n), min(k1, m) + 1))
    X1_probs = [stats.hypergeom.pmf(x1, total_coins, m, k1) for x1 in X1_values]
    
    E_X1Y1 = 0
    E_Y1 = 0
    E_Y1_squared = 0
    
    for i, x1 in enumerate(X1_values):
        prob = X1_probs[i]
        remaining_1euro = m - x1
        remaining_2euro = n - (k1 - x1)
        remaining_total = remaining_1euro + remaining_2euro
        
        # Expected number of 1€ coins lost in afternoon given morning losses
        E_Y1_given_X1 = k2 * (remaining_1euro / remaining_total)
        
        # Variance of Y1 given X1 (hypergeometric)
        D_Y1_given_X1 = k2 * (remaining_1euro / remaining_total) * (remaining_2euro / remaining_total) * (remaining_total - k2) / (remaining_total - 1) if remaining_total > 1 else 0
        
        E_Y1 += E_Y1_given_X1 * prob
        E_X1Y1 += x1 * E_Y1_given_X1 * prob
        E_Y1_squared += (D_Y1_given_X1 + E_Y1_given_X1**2) * prob
    
    D_Y1 = E_Y1_squared - E_Y1**2
    
    # Step 4: Calculate E[Y] and D(Y) - afternoon total losses in value
    E_Y = 2 * k2 - E_Y1
    D_Y = D_Y1
    
    # Step 5: Calculate Covariance and Correlation
    Cov_X1Y1 = E_X1Y1 - E_X1 * E_Y1
    Cov_XY = Cov_X1Y1
    
    correlation = Cov_XY / (np.sqrt(D_X) * np.sqrt(D_Y))
    
    return {
        'E_X1': E_X1, 'D_X1': D_X1,
        'E_X': E_X, 'D_X': D_X,
        'E_Y1': E_Y1, 'D_Y1': D_Y1,
        'E_Y': E_Y, 'D_Y': D_Y,
        'Cov_XY': Cov_XY,
        'correlation': correlation
    }

def verify_with_simulation(m, n, k1, k2, num_simulations=10000):
    """
    Verify results with Monte Carlo simulation
    """
    global X_values, Y_values
    X_values = []
    Y_values = []
    
    for _ in range(num_simulations):
        # Initialize pocket
        pocket = ['1€'] * m + ['2€'] * n
        np.random.shuffle(pocket)
        
        # Morning losses
        morning_loss = np.random.choice(len(pocket), k1, replace=False)
        morning_coins = [pocket[i] for i in morning_loss]
        morning_value = sum(1 if coin == '1€' else 2 for coin in morning_coins)
        
        # Remove morning losses from pocket
        pocket = [pocket[i] for i in range(len(pocket)) if i not in morning_loss]
        
        # Afternoon losses
        if k2 <= len(pocket):
            afternoon_loss = np.random.choice(len(pocket), k2, replace=False)
            afternoon_coins = [pocket[i] for i in afternoon_loss]
            afternoon_value = sum(1 if coin == '1€' else 2 for coin in afternoon_coins)
            
            X_values.append(morning_value)
            Y_values.append(afternoon_value)
    
    # Calculate correlation from simulation
    sim_correlation = np.corrcoef(X_values, Y_values)[0, 1]
    
    return {
        'E_X': np.mean(X_values), 'D_X': np.var(X_values),
        'E_Y': np.mean(Y_values), 'D_Y': np.var(Y_values),
        'correlation': sim_correlation
    }

# Parameters
m, n, k1, k2 = 7, 9, 4, 7

# Calculate theoretical results
results = calculate_correlation_coefficient(m, n, k1, k2)

# Print theoretical results
print("Theoretical Results:")
print(f"E[X] = {results['E_X']:.4f}, D(X) = {results['D_X']:.4f}")
print(f"E[Y] = {results['E_Y']:.4f}, D(Y) = {results['D_Y']:.4f}")
#print esqrt 
sqrtE1 = results['D_X'] + results['E_X']**2
sqrtE2 = results['D_Y'] + results['E_Y']**2 
print(f"E[X]² + D(X) = {sqrtE1:.4f}")
print(f"E[Y]² + D(Y) = {sqrtE2:.4f}")
print(f"Cov(X,Y) = {results['Cov_XY']:.4f}")
print(f"Correlation coefficient = {results['correlation']:.4f}")

# Try to express the result as a simplified fraction
try:
    corr_fraction = Fraction(float(results['correlation'])).limit_denominator(100)
    print(f"Correlation as a fraction: {corr_fraction}")
except:
    pass

# Verify with simulation
print("\nVerifying with simulation...")
sim_results = verify_with_simulation(m, n, k1, k2)
print("Simulation Results:")
print(f"E[X] = {sim_results['E_X']:.4f}, D(X) = {sim_results['D_X']:.4f}")
print(f"E[Y] = {sim_results['E_Y']:.4f}, D(Y) = {sim_results['D_Y']:.4f}")
print(f"Correlation coefficient = {sim_results['correlation']:.4f}")

global X_values, Y_values

# Plot the correlation from simulation
plt.figure(figsize=(8, 6))
plt.scatter(X_values[:500], Y_values[:500], alpha=0.5)
plt.title(f"Morning vs Afternoon Losses Correlation: {sim_results['correlation']:.4f}")
plt.xlabel("Morning Loss Value (X)")
plt.ylabel("Afternoon Loss Value (Y)")
plt.grid(True)
plt.savefig("correlation_plot.png")
plt.show()









# Correlation Coefficient Problem
# I need to find the correlation coefficient between morning and afternoon losses for Jonas, who puts coins in his pocket and loses some throughout the day.

# Given Information
# Jonas puts m = 9 coins of 1€ each day
# Jonas puts n = 6 coins of 2€ each day
# Morning losses are k₁ = 3 coins
# Afternoon losses are k₂ = 4 coins
# Solution Approach
# Let me define random variables:

# X₁ = number of 1€ coins lost in the morning (follows hypergeometric distribution)
# X = total value of morning losses
# Y₁ = number of 1€ coins lost in the afternoon
# Y = total value of afternoon losses
# Step 1: Find E[X₁] and Var(X₁)
# X₁ follows a hypergeometric distribution with parameters (15, 9, 3)

# E[X₁] = 3 × (9/15) = 9/5 = 1.8
# Var(X₁) = 3 × (9/15) × (6/15) × (12/14) ≈ 0.617
# Step 2: Find relationship between X and X₁
# Since 3 coins are lost in the morning:

# X = X₁ × 1€ + (3-X₁) × 2€ = 6€ - X₁
# E[X] = 6 - E[X₁] = 6 - 1.8 = 4.2€
# Var(X) = Var(X₁) ≈ 0.617
# Step 3: Find E[Y₁|X₁] and E[Y₁]
# After morning losses, Jonas has (9-X₁) 1€ coins and (6-(3-X₁)) = 3+X₁ 2€ coins

# E[Y₁|X₁] = 4 × ((9-X₁)/12) = 3 - X₁/3
# E[Y₁] = E[E[Y₁|X₁]] = E[3 - X₁/3] = 3 - E[X₁]/3 = 3 - 1.8/3 = 2.4
# Step 4: Find relationship between Y and Y₁
# Y = Y₁ × 1€ + (4-Y₁) × 2€ = 8€ - Y₁
# E[Y] = 8 - E[Y₁] = 8 - 2.4 = 5.6€
# Var(Y₁) ≈ 0.769 (using law of total variance)
# Var(Y) = Var(Y₁) ≈ 0.769
# Step 5: Calculate Covariance
# E[X₁Y₁] = E[X₁ × E[Y₁|X₁]] = E[X₁(3 - X₁/3)] = 3E[X₁] - E[X₁²]/3
# E[X₁²] = Var(X₁) + E[X₁]² = 0.617 + (9/5)² = 3.857
# E[X₁Y₁] = 3(9/5) - 3.857/3 ≈ 5.4 - 1.286 = 4.114
# Cov(X₁,Y₁) = E[X₁Y₁] - E[X₁]E[Y₁] = 4.114 - (9/5)(12/5) = 4.114 - 4.32 = -0.206
# Cov(X,Y) = Cov(6-X₁, 8-Y₁) = Cov(-X₁,-Y₁) = Cov(X₁,Y₁) = -0.206
# Step 6: Calculate Correlation Coefficient
# ρ = Cov(X,Y) / (√Var(X) × √Var(Y)) = -0.206 / (√0.617 × √0.769) ≈ -0.3

# Answer
# The correlation coefficient between morning and afternoon losses is approximately -0.3.

