

import math
from random import random
from multiprocessing import Pool

from tqdm import tqdm

m = 7
n = 9
k1 = 4
k2 = 7

coins = []

for i in range(m):
    coins.append(1)
    
for i in range(n):
    coins.append(2)
    
def throwing_coinsE1sqrt():
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
        
    return sum1**2, 0  
    
def throwing_coinsE2sqrt():
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
        
    return sum2**2, 0  

def throwing_coinsE1():
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

def throwing_coinsE2():
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

def dispersionD1(avreg):
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
    for i in range(k1):
        dist += coins1[i]
        
    return (dist - avreg) ** 2, 0

def dispersionD2(avreg):
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
        dist += coins2[i]
        
    return (dist - avreg) ** 2, 0

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
        
    sum1 = 0
    sum2 = 0
    
    for i in range(k1):
        sum1 += coins1[i]
        
    for i in range(k2):
        sum2 += coins2[i]    
    
    return sum1 * sum2, 0   
    
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

from functools import partial
if __name__ == '__main__':

    repeat = 100_000_000_0
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    avr1 = parrallel_execution(repeat, num_processes, throwing_coinsE1)
    avr2 = parrallel_execution(repeat, num_processes, throwing_coinsE2)
    
    dispersionWithAvr1 = partial(dispersionD1, avr1)
    dispersionWithAvr2 = partial(dispersionD2, avr2)
    
    # dis1 = parrallel_execution(repeat, num_processes, dispersionWithAvr1)
    # dis2 = parrallel_execution(repeat, num_processes, dispersionWithAvr2)
    
    avr1sqrt = parrallel_execution(repeat, num_processes, throwing_coinsE1sqrt)
    avr2sqrt = parrallel_execution(repeat, num_processes, throwing_coinsE2sqrt)
    
    mathDispersion1 = avr1sqrt - avr1 ** 2
    mathDispersion2 = avr2sqrt - avr2 ** 2
    
    avr12 = parrallel_execution(repeat, num_processes, AverageE12)
    
    qxy = (avr12 - avr1 * avr2) / math.sqrt(mathDispersion1 * mathDispersion2)
    
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # print all the results
    print(f"Average of first: {avr1}")
    print(f"Average of second: {avr2}")
    print(f"Average of both: {avr12}")
    # print(f"Dispersion of first: {dis1}")
    # print(f"Dispersion of second: {dis2}")
    print(f"Dispersion of first math: {mathDispersion1}")
    print(f"Dispersion of second math: {mathDispersion2}")
    print(f"Correlation coefficient: {qxy}")
    