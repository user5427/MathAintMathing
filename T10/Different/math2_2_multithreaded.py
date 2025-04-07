

from random import random
from multiprocessing import Pool

p = 51
q = 69
k = 6

p = p / 100
q = q / 100

def throwing_balls():
    nr = 0
    # throw the balls until both hit
    while True:
        # throw the first ball
        nr += 1
        if random() < p or random() < q:
            return (nr, 0)
            
    return (0, 0)    
    
    
def run_experiment(n):
    count = (0, 0)
    for _ in range(n):
        res = throwing_balls()
        count = (count[0]+res[0], count[1]+res[1])
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
    repeat = 100_000_000
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    result = parallel_execution(repeat, num_processes)
    print(result)
