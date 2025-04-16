

import math
from random import random
from multiprocessing import Pool

from tqdm import tqdm

p = 0.02
q = 0.76


def send_E1():
    oneCount = 1
    
    if random() < q:
        oneCount = 2
        
    return oneCount, 0

def send_E2():   
    message = [0, 1]
    
    if random() < q:
        message[0] = 1
        
    # send the message where the bit flip probability is p
    if random() < p:
        message[0] = 1 - message[0]
    if random() < p:
        message[1] = 1 - message[1]
        
    oneCount = message[0] + message[1]
    
    return oneCount, 0
    
def send_E1_sqrt():
    oneCount = 1
    
    if random() < q:
        oneCount = 2
        
    return oneCount**2, 0

def send_E2_sqrt():   
    message = [0, 1]
    
    if random() < q:
        message[0] = 1
        
    # send the message where the bit flip probability is p
    if random() < p:
        message[0] = 1 - message[0]
    if random() < p:
        message[1] = 1 - message[1]
        
    oneCount = message[0] + message[1]
    
    return oneCount**2, 0

def send_E12():   
    message = [0, 1]
    
    if random() < q:
        message[0] = 1
        
    beforeOneCount = message[0] + message[1]
        
    # send the message where the bit flip probability is p
    if random() < p:
        message[0] = 1 - message[0]
    if random() < p:
        message[1] = 1 - message[1]
        
    oneCount = message[0] + message[1]
    
    return oneCount*beforeOneCount, 0

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

    repeat = 1_000_000_0
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    avr1 = parrallel_execution(repeat, num_processes, send_E1)
    avr2 = parrallel_execution(repeat, num_processes, send_E2)
    
    avr12 = parrallel_execution(repeat, num_processes, send_E12)
    
    cov = avr12 - avr1 * avr2
    
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # print all the results
    print(f"Average of first: {avr1}")
    print(f"Average of second: {avr2}")
    print(f"Average of both: {avr12}")
    print(f"Correlation coefficient: {cov}")
    