

from random import random
from multiprocessing import Pool

n = 16
r = 4
a = 8

balls = []
for i in range(n):
    balls.append(i + 1)

def select_balls():
    balls_copy = balls.copy()
    selected = []
    for _ in range(r):
        index = int(random() * len(balls_copy))
        selected.append(balls_copy.pop(index))
        
    minNr = min(selected)

    if minNr == a:
        return (1, 0)   
    return (0, 0)    
    
    
    
    
def run_experiment(n):
    count = (0, 0)
    for _ in range(n):
        count = (count[0]+select_balls()[0], count[1]+select_balls()[1])
    return count

def parallel_execution(repeat, num_processes):
    chunk_size = repeat // num_processes
    
    # Create a Pool of workers
    with Pool(num_processes) as pool:
        results = pool.map(run_experiment, [chunk_size] * num_processes)
    
    total_count = sum([x[0] for x in results])
    total_count2 = sum([x[1] for x in results])
    return total_count / (repeat+total_count2)

if __name__ == '__main__':
    repeat = 20_000_000
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    result = parallel_execution(repeat, num_processes)
    print(result)
