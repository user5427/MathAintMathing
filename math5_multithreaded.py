

import math
from random import random
from multiprocessing import Pool

from tqdm import tqdm

p = 50

divides = []
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
primes = primes[::-1]

def nums():
    randomnr = random() * p
    randomnr = math.ceil(randomnr)  # avoid division by zero
    
    # choose a random number and see if it divides randomnr, if yes decrement and again choose a random number and do this until we get 1
    count = 0
    while randomnr > 1:
        # check if it divides from the list divides largest to smallest
        
        divided = False
        
        for i in divides[::-1]:
            count += 1
            if randomnr % i == 0:
                randomnr = randomnr // i
                divided = True
                break
            
        # shuffle the primes list to get a random order
        if not divided:
            # check if it divides from the list primes largest to smallest
            for i in primes[::-1]:
                count += 1
                if randomnr % i == 0:
                    randomnr = randomnr // i
                    divided = True
                    break
                
    return count, 0
    
    


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

    repeat = 100_000_00
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    avr1 = parrallel_execution(repeat, num_processes, nums)
    
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # print all the results
    print(f"Average of birbs needed: {avr1}")