

import math
from random import random
from multiprocessing import Pool

from tqdm import tqdm

grades = [5,6,7,8,9,10]  # player indices, representing grades
ppl = 3  # 
def grading():
    gradeList = []
    # pick random grades for each person
    for _ in range(ppl):
        gradeList.append(grades[int(random() * len(grades))])
    # check if exactly two people have the same grade
    if gradeList.count(gradeList[0]) == 2 or gradeList.count(gradeList[1]) == 2 or gradeList.count(gradeList[2]) == 2:
        return 1, 0
    return 0, 0  # if not, return (0, 0)
    
    
    
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
    
    avr1 = parrallel_execution(repeat, num_processes, grading)
    
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # print all the results
    print(f"Average: {avr1}")