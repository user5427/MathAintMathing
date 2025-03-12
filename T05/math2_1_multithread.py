from random import random
from multiprocessing import Pool

pA = 0.5
pB = 0.45

def takingABA():
    aWin = False
    bWin = False
    aWin2 = False
    
    if random() <= pA:
        aWin = True
    if random() <= pB:
        bWin = True
    if random() <= pA:
        aWin2 = True
        
    if aWin and bWin and aWin2:
        return 1
    if aWin and not bWin and aWin2:
        return 1
    if aWin and bWin and not aWin2:
        return 1
    if not aWin and bWin and aWin2:
        return 1
    if not aWin and bWin and not aWin2:
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
    repeat = 3_000_0000
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    result = parallel_execution(repeat, num_processes)
    print(result)
