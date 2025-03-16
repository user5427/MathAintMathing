

from random import random
from multiprocessing import Pool

r = 2.8
r1 = 1.8
r2 = 2.3
n = 9
n1 = 3
n2 = 5
n3 = n - n1 - n2

sphere1Prob = r1 ** 2 / r ** 2
sphere2Prob = (r2 ** 2 - r1 ** 2) / r ** 2
sphere3Prob = 1 - sphere1Prob - sphere2Prob

def birds():
    c1 = 0
    c2 = 0
    c3 = 0
    # tries = 0
    
    # while True:
    #     if sphere1Prob < random():
    #         c1 += 1
    #         tries += 1
        
    #     if tries == n:
    #         break
        
    #     if sphere2Prob < random():
    #         c3 += 1
    #         tries += 1

    #     if tries == n:
    #         break
        
    #     if sphere3Prob < random():
    #         c2 += 1 # not c3 because we are in the third sphere
    #         tries += 1
            
    #     if tries == n:
    #         break
                
    # if c1 == n1 and c2 == n2 and c3 == n3:
    #     return (1, 0)
    # return (0, 0)
    
    # choose x and y coordinates for the sphere and check if they are in the sphere if not choose again
    x = 0
    y = 0
    for _ in range(n):
        x = random() * r
        y = random() * r
        
        while x ** 2 + y ** 2 > r ** 2:
            x = random() * r
            y = random() * r
        
        if x ** 2 + y ** 2 <= r1 ** 2:
            c1 += 1
        elif x ** 2 + y ** 2 <= r2 ** 2:
            c3 += 1
        else:
            c2 += 1
            
    if c1 == n1 and c2 == n2 and c3 == n3:
        return (1, 0)
    return (0, 0)
    

def run_experiment(n):
    count = (0, 0)
    for _ in range(n):
        count = (count[0]+birds()[0], count[1]+birds()[1])
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
    repeat = 2_000_000
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    result = parallel_execution(repeat, num_processes)
    print(result)
