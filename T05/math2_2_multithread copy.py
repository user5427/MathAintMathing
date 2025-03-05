from random import random
from multiprocessing import Pool

pA = 0.64
pB = 0.33

def takingABA():
    bWin = False
    aWin = False
    bWin2 = False
    
    if random() <= pB:
        bWin = True
    if random() <= pA:
        aWin = True
    if random() <= pB:
        bWin2 = True
        
    if bWin and aWin and bWin2:
        return 1
    if bWin and not aWin and bWin2:
        return 1
    
    return 0
        

def run_experiment(n):
    count = 0
    for _ in range(n):
        count += takingABA()
    return count

def parallel_execution(repeat, num_processes):
    chunk_size = repeat // num_processes
    
    # Create a Pool of workers
    with Pool(num_processes) as pool:
        results = pool.map(run_experiment, [chunk_size] * num_processes)
    
    total_count = sum(results)
    return total_count / repeat

if __name__ == '__main__':
    repeat = 30_000_0000
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    result = parallel_execution(repeat, num_processes)
    print(result)
