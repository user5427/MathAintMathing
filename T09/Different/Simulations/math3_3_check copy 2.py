import math
import random
import numpy as np
from multiprocessing import Pool, Array
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from numba import njit
import ctypes  # Needed for shared memory

# --- Setup Parameters ---
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

lamb = math.log(b) / math.log(a)

# --- Simulation Parameters ---
LAMBDA = lamb
NUM_SIMULATIONS = 1_000_000
NUM_THREADS = 16
ANALYZE_COUNT = 10_000

# --- Use Shared Memory ---
shared_array = None  # Global shared array


@njit
def fast_exponential(batch_size, lamb):
    return np.random.exponential(scale=1 / lamb, size=batch_size)

def simulate_batch(batch_size):
    return fast_exponential(batch_size, LAMBDA)

def run_simulation():
    """Run the simulation in parallel using ThreadPoolExecutor."""
    batch_size = NUM_SIMULATIONS // NUM_THREADS
    
    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        futures = [executor.submit(simulate_batch, batch_size) for _ in range(NUM_THREADS)]
        
        durations = []
        for future in tqdm(futures, desc="Simulating"):
            durations.extend(future.result())

    return np.array(durations)


# --- Shared Memory Setup ---
def init_shared_array(durations):
    """Copy `durations` to a shared memory array."""
    global shared_array
    shared_array = Array(ctypes.c_double, len(durations), lock=False)  # 🔥 Fast, no locks!
    
    np_arr = np.frombuffer(shared_array, dtype=np.float64)
    np.copyto(np_arr, durations)  # Copy data into shared memory


@njit
def fast_sample(shared_arr, size):
    """Sample from shared memory array."""
    idx = random.randint(0, size - 1)
    return shared_arr[idx]

def bubbles():
    global shared_array
    np_arr = np.frombuffer(shared_array, dtype=np.float64)
    
    sampled_value = fast_sample(np_arr, len(np_arr))
    return (1, 0) if sampled_value > 4.12 else (0, 0)

def run_experiment(n):
    """Run `n` experiments using `bubbles()`."""
    count = (0, 0)
    for _ in range(n):
        count = (count[0] + bubbles()[0], count[1] + bubbles()[1])
    return count

def parallel_execution():
    """Run experiments in parallel using multiprocessing with shared memory."""
    chunk_size = ANALYZE_COUNT // NUM_THREADS
    
    with Pool(NUM_THREADS, initializer=init_shared_array, initargs=(shared_array,)) as pool:
        results = pool.map(run_experiment, [chunk_size] * NUM_THREADS)
    
    total_count = sum(x[0] for x in results)
    total_count2 = sum(x[1] for x in results)
    
    return total_count / (ANALYZE_COUNT + total_count2) if ANALYZE_COUNT + total_count2 > 0 else 0

# --- Main Execution ---
if __name__ == "__main__":
    durations = run_simulation()
    init_shared_array(durations)  # 🔥 Store in shared memory
    res = parallel_execution()  # Run experiments in parallel
    print(res)
