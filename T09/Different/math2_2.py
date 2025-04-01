import numpy as np
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm  # For progress bars (install with `pip install tqdm`)

p_long = 0.75
x = 5
y = 7
z = 16
lambda_param = -np.log(p_long) / x

# Configuration
NUM_SIMULATIONS = 1_000_000  # Total calls to simulate
NUM_THREADS = 16             # Match CPU cores
LAMBDA = lambda_param        # Rate parameter for the exponential distribution

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
        for future in tqdm(futures, desc="Simulating calls"):
            durations.extend(future.result())
    
    return np.array(durations)

# Analyze results
def analyze(durations):
    probability = np.mean((durations > y) & (durations < z))
    probY = np.mean(durations > y)
    probZ = np.mean(durations < z)
    
    probYandZ = probY + probZ - 1
    print(probYandZ)
    print(f"P({y} < Y < {z}): {probability:.1%}")

if __name__ == "__main__":
    durations = run_simulation()
    analyze(durations)