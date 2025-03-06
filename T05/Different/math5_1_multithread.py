from random import random
from multiprocessing import Pool

p = 0.66

m1 = 6
m2 = 5
m3 = 9

m1pos = []
m2pos = []
m3pos = []

for i in range(10):
    if i != m1:
        m1pos.append(i)
    if i != m2:
        m2pos.append(i)
    if i != m3:
        m3pos.append(i)

original = m1 * 100 + m2 * 10 + m3

def number():
    m1digit = m1
    m2digit = m2
    m3digit = m3
    if random() > p:
        # choose random digit for m1 from m1pos
        m1digit = m1pos[int(random() * len(m1pos))]
        
    if random() > p:
        # choose random digit for m2 from m2pos
        m2digit = m2pos[int(random() * len(m2pos))]
        
    if random() > p:
        # choose random digit for m3 from m3pos
        m3digit = m3pos[int(random() * len(m3pos))]
        
        
    new_number = m1digit * 100 + m2digit * 10 + m3digit
    
    if new_number < original:
        return 1
    return 0
    
    

def run_experiment(n):
    count = 0
    for _ in range(n):
        count += number()
    return count

def parallel_execution(repeat, num_processes):
    chunk_size = repeat // num_processes
    
    # Create a Pool of workers
    with Pool(num_processes) as pool:
        results = pool.map(run_experiment, [chunk_size] * num_processes)
    
    total_count = sum(results)
    return total_count / repeat

if __name__ == '__main__':
    repeat = 20_000_0000
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    result = parallel_execution(repeat, num_processes)
    print(result)
