

import math
from random import random
from multiprocessing import Pool

from tqdm import tqdm

peoples = [0, 1, 2]  # player indices

def ballThrow():
    copyPeople = peoples.copy()
    ballHolder = 0  # player who starts with the ball
    copyPeople.remove(ballHolder)  # remove the player who starts with the ball
    
    for i in range(4):
        newHolder = int(random() * len(copyPeople))  # choose a random player to pass the ball
        tempHoldder = ballHolder
        ballHolder = copyPeople[newHolder]  # update the ball holder
        copyPeople.remove(ballHolder)  # remove the new holder from the list
        copyPeople.append(tempHoldder)  # add the previous holder back to the list
        if ballHolder == 0 and i < 3:  # if the ball holder is the starting player before the last pass
            return (0, 0)
        
    return (1, 0) if ballHolder == 0 else (0, 0)  # return whether the ball holder is the starting player

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
    
    avr1 = parrallel_execution(repeat, num_processes, ballThrow)
    
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # print all the results
    print(f"Average: {avr1}")