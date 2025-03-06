from random import random
from multiprocessing import Pool

p = 0.44
m = 4
n = 7

def saulys():
    tries = 0
    hitTarget = False
    # hits = 0
    # saulys bando numusti taikini su tikimybe p, jis gali kartoti tai n kartu
    for _ in range(n):
        tries += 1
        if random() <= p:
            # hits += 1
            hitTarget = True
            break
        
    if hitTarget == False:
        return 0
    else:
        if tries <= m:
            return 1
        return 0
    
    # if hits <= m:
    #     return 1
    # return 0

def run_experiment(n):
    count = 0
    for _ in range(n):
        count += saulys()
    return count

def parallel_execution(repeat, num_processes):
    chunk_size = repeat // num_processes
    
    # Create a Pool of workers
    with Pool(num_processes) as pool:
        results = pool.map(run_experiment, [chunk_size] * num_processes)
    
    total_count = sum(results)
    return total_count / repeat

if __name__ == '__main__':
    repeat = 10_000_0000
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    result = parallel_execution(repeat, num_processes)
    print(result)
