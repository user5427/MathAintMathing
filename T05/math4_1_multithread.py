from random import random
from multiprocessing import Pool

r = 0.08
size = 1

def droplets():
    x = random()
    y = random()
    
    if x < r or y < r or x > size - r or y > size - r:
        return 1
    return 0
    

def run_experiment(n):
    count = 0
    for _ in range(n):
        count += droplets()
    return count

def parallel_execution(repeat, num_processes):
    chunk_size = repeat // num_processes
    
    # Create a Pool of workers
    with Pool(num_processes) as pool:
        results = pool.map(run_experiment, [chunk_size] * num_processes)
    
    total_count = sum(results)
    return total_count / repeat

if __name__ == '__main__':
    repeat = 20_000_0000
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    result = parallel_execution(repeat, num_processes)
    print(result)
