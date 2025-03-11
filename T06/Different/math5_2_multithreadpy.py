

from random import random
from multiprocessing import Pool

white = 5
black = 10

n = 7
k = 4

whiteProb = white / (white + black)
blackProb = 1 - whiteProb


def balls():
    whiteCount = 0
    for _ in range(n):
        if random() <= whiteProb:
            whiteCount += 1
            
    repeatWhite = 0
    
    for _ in range(whiteCount):
        if random() <= whiteProb:
            repeatWhite += 1
            
    if repeatWhite + whiteCount == k:
        return (1, 0)
    return (0, 0)
    
def run_experiment(n):
    count = (0, 0)
    for _ in range(n):
        count = (count[0]+balls()[0], count[1]+balls()[1])
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
