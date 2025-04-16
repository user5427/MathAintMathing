

import math
from random import random
from multiprocessing import Pool

from tqdm import tqdm

p = 0.65

def birds():
    # we need male and female bird so we need one of each
    male = 0
    female = 0
    
    while male == 0 or female == 0:
        if random() < p:
            female += 1
        else:
            male += 1
        
    return male + female, 0


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

    repeat = 500_00000
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    # averages = []
    # for i in range(100):
    #     avr1 = parrallel_execution(repeat, num_processes, birds)
    #     averages.append(avr1)
        
    # avr1 = sum(averages) / len(averages)
    
    avr1 = parrallel_execution(repeat, num_processes, birds)
    
    
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # print all the results
    print(f"Average of birbs needed: {avr1}")