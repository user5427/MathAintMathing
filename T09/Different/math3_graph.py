import math
import numpy as np


h = 14
m = 456
alfa = 0.89
p = 54
n = 1000

halfProb = 0.5 

prob = m / n
opProb = 1 - prob

invProb = 1 / opProb
sqrProb = invProb ** (1 / h)

b = sqrProb
a = math.e

lamb = math.log (b) / math.log (a)


import matplotlib.pyplot as plt

# Define the function for the probability graph
def probability_function(x, lamb):
    return math.e ** (-lamb * x)

# Generate x values
x_values = np.linspace(0, 20, 1000)  # Adjust range and resolution as needed

# Compute y values
y_values = [probability_function(x, lamb) for x in x_values]

# Plot the graph
plt.plot(x_values, y_values, label="e^(-λx)")
plt.title("Probability Graph")
plt.xlabel("x")
plt.ylabel("Probability")
plt.legend()
plt.grid()
plt.show()