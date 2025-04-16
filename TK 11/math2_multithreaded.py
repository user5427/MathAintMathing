

import math
from random import random
from multiprocessing import Pool

from tqdm import tqdm

N = 57
k = 15
n = 5

fishes = []

for i in range(N-k):
    fishes.append('f')
    
for i in range(k):
    fishes.append('k')



def fishies():
    copyFishes = fishes.copy()
    
    takenBalls = []
    
    for i in range(n):
        rand = random()
        index = int(rand * len(copyFishes))
        takenBalls.append(copyFishes[index])
        copyFishes.pop(index)
        
    # count the number of red and blue balls
    normal = 0
    colored = 0
    for ball in takenBalls:
        if ball == 'f':
            normal += 1
        else:
            colored += 1
            
    if colored > 0:
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
    
    res1 = parrallel_execution(repeat, num_processes, fishies)
    
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # print all the results
    print(f"{res1}")