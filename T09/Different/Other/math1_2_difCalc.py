

from random import random
from multiprocessing import Pool

a = 11.0
b = 5.0
x = 2.21 

bFor = b
aFor = -b / a

eVal = 0.1

def triangle():
    aRand = random() * a
    bRand = random() * b
    
    # a and b are the two sides of the triangle
    # check if the (aRand, bRand) is inside the triangle, NO TOUCHY THE X VALUE!!!
    
    yNow = aFor * aRand + bFor
    
    if bRand > yNow:
        return (0, -1)
    
    if bRand < x:
        return (1, 0)
    return (0, 0)
    
def run_experiment(n):
    count = (0, 0)
    for _ in range(n):
        count = (count[0]+triangle()[0], count[1]+triangle()[1])
    return count

def parallel_execution(repeat, num_processes):
    global x
    
    chunk_size = repeat // num_processes
    
    # Create a Pool of workers
    tempX = x
    x = x + eVal
    with Pool(num_processes) as pool:
        results = pool.map(run_experiment, [chunk_size] * num_processes)
    
    total_count = sum([x[0] for x in results])
    total_count2 = sum([x[1] for x in results])
    
    res1 =  total_count / (repeat+total_count2)
    
    x = tempX - eVal
    with Pool(num_processes) as pool:
        results = pool.map(run_experiment, [chunk_size] * num_processes)
        
    total_count = sum([x[0] for x in results])
    total_count2 = sum([x[1] for x in results])
    
    res2 =  total_count / (repeat+total_count2)
    
    return (res1 - res2) / (2 * eVal)

if __name__ == '__main__':
    repeat = 100_000
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    result = parallel_execution(repeat, num_processes)
    print(result)
