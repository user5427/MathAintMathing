

from random import random
from multiprocessing import Pool

a = 52.03
b = 3.44
k = 16
c = 3.62

inc = 0
def line():
    global inc
    point = inc * b
    inc += 1 / 20_000_000
    y = k * point + c
    
    if y < a:
        return (1, 0)
    return (0, 0)
    
def run_experiment(n):
    count = (0, 0)
    for _ in range(n):
        res = line()
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
    repeat = 320_000_000
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    result = parallel_execution(repeat, num_processes)
    print(result)
