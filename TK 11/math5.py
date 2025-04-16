

import math
from random import random
from multiprocessing import Pool

from tqdm import tqdm

a = 14
b = 18
c = 18
d = 27

firstBox = []
secondBox = []

for i in range(a):
    firstBox.append('b')
for i in range(b):
    firstBox.append('j')
for i in range(c):
    secondBox.append('b')
for i in range(d):
    secondBox.append('j')

boxProb = 0.5

def balls():
    if random() < boxProb:
        copyBallList = firstBox.copy()
        # take first ball and check if its white then take the second ball and check if its white
        # if both are white then return 1 else return 0
        firstBall = copyBallList.pop(int(random() * len(copyBallList)))
        secondBall = copyBallList.pop(int(random() * len(copyBallList)))
        if firstBall == 'b' and secondBall == 'b':
            return 1, 0
    else:
        copyBallList = secondBox.copy()
        firstBall = copyBallList.pop(int(random() * len(copyBallList)))
        secondBall = copyBallList.pop(int(random() * len(copyBallList)))
        if firstBall == 'b' and secondBall == 'b':
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

    repeat = 1_000_000_00
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    res1 = parrallel_execution(repeat, num_processes, balls)
    
    import os
    # os.system('cls' if os.name == 'nt' else 'clear')
    
    # print all the results
    print(f"{res1}")