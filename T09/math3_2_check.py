import numpy as np
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm  # For progress bars (install with `pip install tqdm`)

import math


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

# print(lamb)

invHalf = 1 / halfProb
sqrHalf = invHalf ** (1 / lamb)
h0 = math.log (sqrHalf) / math.log (a)
print(f"(1) specifine tikimybe: {halfProb} aukstis {h0}")


safety = (1 / alfa) ** (1 / lamb)

height = math.log (safety) / math.log (a)
print(f"(2) saugus aukstis - tikimybe: {alfa} aukstis {height}")


increased = height * (1 + p / 100)
prob = math.e ** (- lamb * increased)
print(f"(3) padidintas saugus aukstis - tikimybe: {prob} aukstis {increased}")

# Configuration
NUM_SIMULATIONS = 10_000_000  # Total calls to simulate
NUM_THREADS = 16             # Match CPU cores
LAMBDA = lamb        # Rate parameter for the exponential distribution

# Simulate a batch of calls (thread-safe)
def simulate_batch(batch_size):
    return np.random.exponential(scale=1/LAMBDA, size=batch_size)

# Main simulation (parallelized)
def run_simulation():
    batch_size = NUM_SIMULATIONS // NUM_THREADS
    futures = []
    
    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        # Submit batches to threads
        for _ in range(NUM_THREADS):
            futures.append(executor.submit(simulate_batch, batch_size))
        
        # Collect results (with progress bar)
        durations = []
        for future in tqdm(futures, desc="Simulating spiders"):
            durations.extend(future.result())
    
    return np.array(durations)

# Analyze results
def analyze(durations):
    probability = np.mean((durations > height))
    print(probability)

if __name__ == "__main__":
    durations = run_simulation()
    analyze(durations)