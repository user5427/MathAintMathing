

import math
from random import random
from multiprocessing import Pool

from tqdm import tqdm

m = 99
n = 1506
p = 7
q = 3

difference = n - m
def kartotinis():
    
    num = m + difference * random()
    num = int(num)
    
    if num % p == 0 or num % q == 0:
        return 1, 0
    return 0, 0


def run_experiment(args):
    n, position, func = args
    count = (0, 0)
    
    iterator = tqdm(range(n), position=position, desc=f"Proc {position} only", leave=True, ascii=True) if position <= 0 else range(n)
    
    for _ in iterator:
        res = func()
        count = (count[0]+res[0], count[1]+res[1])
    return count

def parrallel_execution(repeat, num_processes, func):
    chunk_size = repeat // num_processes
    args = [(chunk_size, i, func) for i in range(num_processes)]
    
    # Create a Pool of workers
    with Pool(num_processes) as pool:
        results = pool.map(run_experiment, args)
    
    total_count = sum([x[0] for x in results])
    total_count2 = sum([x[1] for x in results])
    return total_count / (repeat+total_count2)

if __name__ == '__main__':

    repeat = 1_000_000_000
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    res1 = parrallel_execution(repeat, num_processes, kartotinis)
    
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # print all the results
    print(f"{res1}")