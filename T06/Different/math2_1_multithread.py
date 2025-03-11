

from random import random
from multiprocessing import Pool

p = 0.59
n = 6
m = 3

def shooter():
    # each targer shooter shoots twice
    # wins count as successfully shooting twice the target
    wins = 0

    # n targets
    for _ in range(n):
        winsTemp = 0
        for _ in range(2):
            if random() <= p:
                winsTemp += 1
        if winsTemp == 2:
            wins += 1
            
    if wins == m:
        return (1, 0)
    return (0, 0)
    
def run_experiment(n):
    count = (0, 0)
    for _ in range(n):
        count = (count[0]+shooter()[0], count[1]+shooter()[1])
    return count

def parallel_execution(repeat, num_processes):
    chunk_size = repeat // num_processes
    
    # Create a Pool of workers
    with Pool(num_processes) as pool:
        results = pool.map(run_experiment, [chunk_size] * num_processes)
    
    total_count = sum([x[0] for x in results])
    total_count2 = sum([x[1] for x in results])
    return total_count / (repeat+total_count2)

if __name__ == '__main__':
    repeat = 30_000_000
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    result = parallel_execution(repeat, num_processes)
    print(result)
