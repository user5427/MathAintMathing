from multiprocessing import Pool
import random
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import math

# USER CONFIGURATION START
# USER CONFIGURATION START
# USER CONFIGURATION START

p = 0.26
t = 30
lamb = math.log((1 / p) ** (1 / t)) / math.log(math.e)

T = 16
n = 5

count = 3

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
def fishers(durations):
    list = []
    for i in range(n):
        list.append(fast_sample(durations))
        
        
    # find all that are below T
    below = [x for x in list if x <= T]
    
    # check if its only count
    if len(below) == count:
        return 1, 0
    return 0, 1
    
    
def run_experiment(args):
    durations, n = args  # Unpack arguments since Pool.map only supports one argument
    count = (0, 0)
    for _ in range(n):
        count = (count[0] + fishers(durations)[0], count[1] + fishers(durations)[1])
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
