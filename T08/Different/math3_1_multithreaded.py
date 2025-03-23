

from random import random
from multiprocessing import Pool

p1 = 0.59
p2 = 0.69
m = 6
 


def throwingBalls():
    p1Balls = 0
    p2Balls = 0
    
    # throwing balls until they fail
    while random() < p1:
        p1Balls += 1
        
    while random() < p2:
        p2Balls += 1
        
    if p1Balls < m and p2Balls < m:
        return (1, 0)
    return (0, 0)
    
    
def run_experiment(n):
    count = (0, 0)
    for _ in range(n):
        count = (count[0]+throwingBalls()[0], count[1]+throwingBalls()[1])
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
