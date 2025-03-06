from random import random
from multiprocessing import Pool

white = 28
black = 100 - white
k = 2

def taking():
    whiteProb = white / (white + black)
    whitCount = 0
    turnNr = 0
    
    while whitCount < k:
        if random() < whiteProb:
            whitCount += 1
            
        if whitCount == k:
            return 1 if turnNr == 0 else 0
        
        turnNr += 1
        if turnNr >= 2:
            turnNr = 0
    
    return 0

def run_experiment(n):
    count = 0
    for _ in range(n):
        count += taking()
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
