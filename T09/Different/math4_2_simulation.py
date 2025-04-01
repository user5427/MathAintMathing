from multiprocessing import Pool
import random
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import math

# USER CONFIGURATION START
# USER CONFIGURATION START
# USER CONFIGURATION START

r = 79
t = 18.0
n = 7
T = 33.0
alfa = 0.47          

r = r / 100

lamb = math.log((1 / r) ** (1 / t)) / math.log(math.e)

# USER CONFIGURATION END
# USER CONFIGURATION END
# USER CONFIGURATION END

# --- Simulation Parameters ---
LAMBDA = lamb
NUM_SIMULATIONS = 5_000_000
NUM_THREADS = 16
ANALYZE_COUNT = 1_000_000_0

# --- Simulation Function ---
def simulate_batch(batch_size):
    """Generate a batch of exponentially distributed random values."""
    return np.random.exponential(scale=1/LAMBDA, size=batch_size)

def run_simulation():
    """Run the simulation in parallel using ThreadPoolExecutor."""
    batch_size = NUM_SIMULATIONS // NUM_THREADS
    
    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        futures = [executor.submit(simulate_batch, batch_size) for _ in range(NUM_THREADS)]
        
        durations = []
        for future in tqdm(futures, desc="Simulating"):
            durations.extend(future.result())

    return np.array(durations)  # Return durations instead of using global variable

def fast_sample(durations):
    idx = random.randint(0, len(durations) - 1)  # 🔥 Faster than NumPy!
    return durations[idx]

# --- Business Logic ---
def bubbles(durations):
    list = []
    for i in range(n):
        list.append(fast_sample(durations))
        
    smallest = min(list)
    second_smallest = sorted(list)[1]  # Get the second smallest value
    
    # time between the two smallest values is larger than T
    if second_smallest - smallest > T:
        return (1, 0)
    else:
        return (0, 0)
    
    
def run_experiment(args):
    durations, n = args  # Unpack arguments since Pool.map only supports one argument
    count = (0, 0)
    for _ in range(n):
        count = (count[0] + bubbles(durations)[0], count[1] + bubbles(durations)[1])
    return count

# --- Parallel Execution with Multiprocessing ---
def parallel_execution(durations):
    """Run multiple experiments in parallel using multiprocessing.Pool."""
    chunk_size = ANALYZE_COUNT // NUM_THREADS
    
    with Pool(NUM_THREADS) as pool:
        results = pool.map(run_experiment, [(durations, chunk_size)] * NUM_THREADS)
    
    total_count = sum(x[0] for x in results)
    total_count2 = sum(x[1] for x in results)
    
    return total_count / (ANALYZE_COUNT + total_count2) if ANALYZE_COUNT + total_count2 > 0 else 0  # Prevent division by zero

# --- Main Execution ---
if __name__ == "__main__":
    durations = run_simulation()  # Generate durations
    res = parallel_execution(durations)  # Run experiments in parallel
    print(res)
