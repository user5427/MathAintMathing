# import numpy as np
# import matplotlib.pyplot as plt

# # Step 1: Define lambda from P(Y > 30) = 10%
# p_long = 0.10  # P(Y > 30) = 10%
# x = 30         # Threshold (minutes)
# lambda_param = -np.log(p_long) / x  # λ ≈ 0.007675

# # Step 2: Simulate call durations
# n_simulations = 10_000
# simulated_durations = np.random.exponential(scale=1/lambda_param, size=n_simulations)

# # Step 3: Plot histogram vs theoretical PDF
# plt.figure(figsize=(10, 6))

# # Plot histogram of simulated data
# plt.hist(
#     simulated_durations, 
#     bins=50, 
#     density=True, 
#     alpha=0.6, 
#     color='blue', 
#     label='Simulated Durations'
# )

# # Plot theoretical exponential PDF
# y_vals = np.linspace(0, 120, 1000)
# pdf_vals = lambda_param * np.exp(-lambda_param * y_vals)
# plt.plot(
#     y_vals, 
#     pdf_vals, 
#     'r-', 
#     linewidth=2, 
#     label=f'Exponential PDF (λ={lambda_param:.4f})'
# )

# # Add vertical lines for key percentiles
# plt.axvline(x=30, color='green', linestyle='--', label='P(Y > 30) = 10%')
# plt.axvline(x=10, color='purple', linestyle='--', label='P(Y ≤ 10) ≈ 7.4%')

# # Customize the plot
# plt.title('Simulated Call Durations vs Exponential Distribution', fontsize=14)
# plt.xlabel('Call Duration (minutes)', fontsize=12)
# plt.ylabel('Probability Density', fontsize=12)
# plt.legend(fontsize=10)
# plt.grid(True, alpha=0.2)

# # Show the plot
# plt.show()

# # Step 4: Print key statistics
# print(f"Simulated P(Y > 30): {np.mean(simulated_durations > 30):.1%}")
# print(f"Simulated P(Y ≤ 10): {np.mean(simulated_durations <= 10):.1%}")



import numpy as np
import matplotlib.pyplot as plt

p_long = 0.75
x = 5
lambda_param = -np.log(p_long) / x

# Define theoretical functions
def exponential_cdf(y):
    return 1 - np.exp(-lambda_param * y)

def exponential_pdf(y):
    return lambda_param * np.exp(-lambda_param * y)

# Example calculations
y1 = 7  # P(Y ≤ 10)
y2 = 30  # P(Y > 30)

P_leq_10 = exponential_cdf(y1)
P_gt_30 = np.exp(-lambda_param * y2)

print(f"P(Y ≤ {y1}): {P_leq_10:.8%}") 
print(f"P(Y > {y2}): {P_gt_30:.8%}") 