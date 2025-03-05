from random import random
from multiprocessing import Pool

n = 3.093744489
remaining = 0.093744489+0.015
dropletSize = 0.08

goodSize = (1 - dropletSize*2)**2
badSize = 1 - goodSize

def droplets():
    yPosition1 = random()
    yPosition2 = random()
    yPosition3 = random()
    yPosition4 = random()
    
    if yPosition1 <= badSize:
        return 1
    
    if yPosition2 <= badSize:
        return 1
    
    if yPosition3 <= badSize:
        return 1
    
    if random() <= remaining:
        if yPosition4 <= badSize:
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
