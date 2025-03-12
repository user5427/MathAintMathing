

from random import random
from multiprocessing import Pool

p0 = 0.11
p1 = 0.37
p2 = 1 - p0 - p1
n = 5
pointLimit = 2*n-2

def exams():
    points = 0
    for _ in range(n):
        x = random()
        if p0 < x < p0 + p1:
            points += 1
        elif p0 + p1 < x < p0 + p1 + p2:
            points += 2

    if points >= pointLimit:
        return (1, 0)
    return (0, 0)            
    
def run_experiment(n):
    count = (0, 0)
    for _ in range(n):
        count = (count[0]+exams()[0], count[1]+exams()[1])
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
