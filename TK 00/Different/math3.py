

import math
from random import random
from multiprocessing import Pool
import random

from tqdm import tqdm

n = 15
k = 7


def numbers():
    numberList = []
    # fill the list from 1 to 15 and shuffle it
    for i in range(1, 16):
        numberList.append(i)
        
    random.shuffle(numberList)
    
    # chekc if atleast k numbers are in order (that is i - 1 will be in the left of i, i = 2, 3, ..., k)
    foundGud = False
    for j in range (0, n - k):
        foundGud = True
        for i in range(j, k + j):
            if numberList[i] < numberList[i-1]:
                pass
            else:
                foundGud = False
                break
            
    if foundGud:
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

    repeat = 1_000_000_0
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    res1 = parrallel_execution(repeat, num_processes, numbers)
    
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # print all the results
    print(f"{res1}")