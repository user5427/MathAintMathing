

import math
from random import random
from multiprocessing import Pool

from tqdm import tqdm

pictures = 8
colored = 1
takes = 5

picturesList = []
for i in range(pictures):
    if i < colored:
        picturesList.append(1)  # 1 represents a colored picture
    else:
        picturesList.append(0)  # 0 represents a non-colored picture

def pictures():
    picturesCopy = picturesList.copy()

    taken = []
    for _ in range(takes):
        picture = int(random() * len(picturesCopy))  # pick a random picture
        taken.append(picturesCopy[picture])  # add the picture to the taken list
        picturesCopy.pop(picture)  # remove the picture from the deck

    #check if the second picture is colored
    if len(taken) > 1 and taken[1] == 1:
        return (1, 0)
    
    return (0, 0)    
    
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

    repeat = 100_000_000
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    avr1 = parrallel_execution(repeat, num_processes, pictures)
    
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # print all the results
    print(f"Average: {avr1}")