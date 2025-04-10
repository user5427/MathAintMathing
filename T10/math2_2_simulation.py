from multiprocessing import Pool
import random
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import math

# USER CONFIGURATION START
# USER CONFIGURATION START
# USER CONFIGURATION START

lamb1 = 1.43
lamb2 = 0.86

# USER CONFIGURATION END
# USER CONFIGURATION END
# USER CONFIGURATION END

# --- Simulation Parameters ---
NUM_SIMULATIONS = 5_000_000
NUM_THREADS = 16
ANALYZE_COUNT = 1_000_000

# --- Simulation Function ---
def simulate_batch(batch_size, lamb):
    """Generate a batch of exponentially distributed random values."""
    return np.random.exponential(scale=1/lamb, size=batch_size)

def run_simulation(lamb):
    """Run the simulation in parallel using ThreadPoolExecutor."""
    batch_size = NUM_SIMULATIONS // NUM_THREADS
    
    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        futures = [executor.submit(simulate_batch, batch_size, lamb) for _ in range(NUM_THREADS)]
        
        durations = []
        for future in tqdm(futures, desc="Simulating"):
            durations.extend(future.result())

    return np.array(durations)  # Return durations instead of using global variable

def fast_sample(durations):
    idx = random.randint(0, len(durations) - 1)  # 🔥 Faster than NumPy!
    return durations[idx]

# --- Business Logic ---
def clients(durations):
    first = fast_sample(durations[0])  # Sample first duration
    second = fast_sample(durations[1])  # Sample second duration
    
    if first < second:
        # If first process "wins", we wait according to second process rate
        return second, 0
    else:
        # If second process "wins", we wait according to first process rate
        return first, 0
    
from tqdm import tqdm

def run_experiment(args):
    durations, n, position = args  # Position tells tqdm which line to print on
    count = (0, 0)
    
    iterator = tqdm(range(n), position=position, desc=f"Proc {position} only", leave=True, ascii=True) if position <= 0 else range(n)
    
    for _ in iterator:
        exp = clients(durations)
        count = (count[0] + exp[0], count[1] + exp[1])
    return count

# --- Parallel Execution with Multiprocessing ---
def parallel_execution(durations):
    chunk_size = ANALYZE_COUNT // NUM_THREADS
    args_list = [(durations, chunk_size, i) for i in range(NUM_THREADS)]

    with Pool(NUM_THREADS) as pool:
        results = pool.map(run_experiment, args_list)

    total_count = sum(x[0] for x in results)
    total_count2 = sum(x[1] for x in results)
    
    return total_count / (ANALYZE_COUNT + total_count2) if ANALYZE_COUNT + total_count2 > 0 else 0

# --- Main Execution ---
if __name__ == "__main__":
    durations1 = run_simulation(lamb1)  # Generate durations
    durations2 = run_simulation(lamb2)  # Generate durations    
    durations = (durations1, durations2)  # Combine durations
    res = parallel_execution(durations)  # Run experiments in parallel
    
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(res)
