

import math
from random import random
from multiprocessing import Pool

from tqdm import tqdm

m = 8
n = 8
k1 = 6
k2 = 6

coins = []

for i in range(m):
    coins.append(1)
    
for i in range(n):
    coins.append(2)

def throwing_ballsE2():
    # take k1 coins and then k2 coins
    myCoins = coins.copy()
    
    coins1 = []
    coins2 = []
    
    for i in range(k1):
        index = int(random() * len(myCoins))
        coins1.append(myCoins[index])
        myCoins.remove(myCoins[index])
        
    for i in range(k2):
        index = int(random() * len(myCoins))
        coins2.append(myCoins[index])
        myCoins.remove(myCoins[index]) 
        
    sum2 = 0
    
    for i in range(k2):
        sum2 += coins2[i]
        
    return sum2, 0  

def throwing_ballsE1():
    # take k1 coins and then k2 coins
    myCoins = coins.copy()
    
    coins1 = []
    coins2 = []
    
    for i in range(k1):
        index = int(random() * len(myCoins))
        coins1.append(myCoins[index])
        myCoins.remove(myCoins[index])
        
    for i in range(k2):
        index = int(random() * len(myCoins))
        coins2.append(myCoins[index])
        myCoins.remove(myCoins[index]) 
        
    sum1 = 0
    
    for i in range(k1):
        sum1 += coins1[i]
        
    return sum1, 0  

def dispersionD2():
    myCoins = coins.copy()
    
    coins1 = []
    coins2 = []
    
    for i in range(k1):
        index = int(random() * len(myCoins))
        coins1.append(myCoins[index])
        myCoins.remove(myCoins[index])
        
    for i in range(k2):
        index = int(random() * len(myCoins))
        coins2.append(myCoins[index])
        myCoins.remove(myCoins[index]) 
        
    dist = 0
    global avr2
    for i in range(k2):
        dist += (avr2 - coins2[i]) ** 2
        
    return dist, 0
    
def dispersionD1():
    myCoins = coins.copy()
    
    coins1 = []
    coins2 = []
    
    for i in range(k1):
        index = int(random() * len(myCoins))
        coins1.append(myCoins[index])
        myCoins.remove(myCoins[index])
        
    for i in range(k2):
        index = int(random() * len(myCoins))
        coins2.append(myCoins[index])
        myCoins.remove(myCoins[index]) 
        
    dist = 0
    global avr1
    for i in range(k1):
        dist += (avr1 - coins1[i]) ** 2
        
    return dist, 0

def AverageE12(): 
        # take k1 coins and then k2 coins
    myCoins = coins.copy()
    
    coins1 = []
    coins2 = []
    
    for i in range(k1):
        index = int(random() * len(myCoins))
        coins1.append(myCoins[index])
        myCoins.remove(myCoins[index])
        
    for i in range(k2):
        index = int(random() * len(myCoins))
        coins2.append(myCoins[index])
        myCoins.remove(myCoins[index]) 
        
    sum = 0
    
    for i in range(k1):
        for j in range(k2):
            sum += coins1[i] + coins2[j]
        
    return sum, 0     
    
def run_experiment(args):
    n, position, func = args
    count = (0, 0)
    
    iterator = tqdm(range(n), position=position, desc=f"Proc {position} only", leave=True, ascii=True) if position <= 0 else range(n)
    
    for _ in iterator:
        res = func()
        count = (count[0]+res[0], count[1]+res[1])
    return count

def parallel_execution(repeat, num_processes, func):
    chunk_size = repeat // num_processes
    args = [(chunk_size, i, func) for i in range(num_processes)]
    
    # Create a Pool of workers
    with Pool(num_processes) as pool:
        results = pool.map(run_experiment, args)
    
    total_count = sum([x[0] for x in results])
    total_count2 = sum([x[1] for x in results])
    return total_count / (repeat+total_count2)


global avr2
avr2 = 0

global avr1
avr1 = 0

if __name__ == '__main__':

    repeat = 100_000_0
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    avr1 = parallel_execution(repeat, num_processes, throwing_ballsE1)
    avr2 = parallel_execution(repeat, num_processes, throwing_ballsE2)
    
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    dis1 = parallel_execution(repeat, num_processes, dispersionD1)
    dis2 = parallel_execution(repeat, num_processes, dispersionD2)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    avr12 = parallel_execution(repeat, num_processes, AverageE12)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
    qxy = (avr12 - avr1 * avr2) / math.sqrt(dis1 * dis2)
    
    # print all the results
    print(f"Average of first: {avr1}")
    print(f"Average of second: {avr2}")
    print(f"Average of both: {avr12}")
    print(f"Dispersion of first: {dis1}")
    print(f"Dispersion of second: {dis2}")
    print(f"Correlation coefficient: {qxy}")
    