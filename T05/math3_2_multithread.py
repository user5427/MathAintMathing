from random import random
from multiprocessing import Pool

p1 = 0.6
p2 = 0.85
p3 = 0.62

def judges():
    p1Corr = False
    p2Corr = False
    p3Corr = False
    
    correctCount = 0
    
    if random() <= p1:
        correctCount += 1
        p1Corr = True
        
    if random() <= p2:
        correctCount += 1
        p2Corr = True
        
    if random() <= p3:
        correctCount += 1
        p3Corr = True
        
    if correctCount <= 1:
        return (0, -1)
        
    if correctCount >= 2 and p1Corr:
        return (1, 0)
    else:
        return (0, 0)
        

def run_experiment(n):
    count = (0, 0)
    for _ in range(n):
        count = (count[0]+judges()[0], count[1]+judges()[1])
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
    repeat = 10_000_0000
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    result = parallel_execution(repeat, num_processes)
    print(result)
