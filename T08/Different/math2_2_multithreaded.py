

from random import random
from multiprocessing import Pool

n = 61
a = 21
b = 18
x = 226.48


def sellingStuff():
    sold = n * random()
    profit = sold * a - (n - sold) * b
    
    if profit >= 0:  
        return (1, 0)
    return (0, 0)
    
    
    
def run_experiment(n):
    count = (0, 0)
    for _ in range(n):
        count = (count[0]+sellingStuff()[0], count[1]+sellingStuff()[1])
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
    repeat = 20_000_000
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    result = parallel_execution(repeat, num_processes)
    print(result)
