

import math
from random import random
from multiprocessing import Pool

from tqdm import tqdm

m0 = 6
m1 = 6
m2 = 4

coins = []

for i in range(m0):
    coins.append(0)
    
for i in range(m1):
    coins.append(1)

for i in range(m2):
    coins.append(2)


def lotteryAvrX():
    copy = coins.copy()
    
    # choose three random coins
    choosenCoins = []
    for i in range(3):
        choosenCoins.append(copy.pop(int(random() * len(copy))))
        
    # totalSum = 0
    twoCoins = 0
    for i in range(3):
        # totalSum += choosenCoins[i]
        if choosenCoins[i] == 2:
            twoCoins += 1
            
    return twoCoins, 0

def lotteryAvrXS():
    copy = coins.copy()
    
    # choose three random coins
    choosenCoins = []
    for i in range(3):
        choosenCoins.append(copy.pop(int(random() * len(copy))))
        
    totalSum = 0
    twoCoins = 0
    for i in range(3):
        totalSum += choosenCoins[i]
        if choosenCoins[i] == 2:
            twoCoins += 1
            
    return twoCoins * totalSum, 0
            
def lotteryAvrS():
    copy = coins.copy()
    
    # choose three random coins
    choosenCoins = []
    for i in range(3):
        choosenCoins.append(copy.pop(int(random() * len(copy))))
        
    totalSum = 0
    for i in range(3):
        totalSum += choosenCoins[i]
            
    return totalSum, 0

def lotteryDispersionX(average_x):
    copy = coins.copy()
    
    # choose three random coins
    choosenCoins = []
    for i in range(3):
        choosenCoins.append(copy.pop(int(random() * len(copy))))
        
    # totalSum = 0
    twoCoins = 0
    for i in range(3):
        # totalSum += choosenCoins[i]
        if choosenCoins[i] == 2:
            twoCoins += 1
            
    return (twoCoins - average_x) ** 2, 0

def lotteryDispersionS(average_s):
    copy = coins.copy()
    
    # choose three random coins
    choosenCoins = []
    for i in range(3):
        choosenCoins.append(copy.pop(int(random() * len(copy))))
        
    totalSum = 0
    for i in range(3):
        totalSum += choosenCoins[i]
            
    return (totalSum - average_s) ** 2, 0


def lotteryAvrXSquere():
    copy = coins.copy()
    
    # choose three random coins
    choosenCoins = []
    for i in range(3):
        choosenCoins.append(copy.pop(int(random() * len(copy))))
        
    # totalSum = 0
    twoCoins = 0
    for i in range(3):
        # totalSum += choosenCoins[i]
        if choosenCoins[i] == 2:
            twoCoins += 1
            
    return twoCoins**2, 0
            
def lotteryAvrSSquere():
    copy = coins.copy()
    
    # choose three random coins
    choosenCoins = []
    for i in range(3):
        choosenCoins.append(copy.pop(int(random() * len(copy))))
        
    totalSum = 0
    for i in range(3):
        totalSum += choosenCoins[i]
            
    return totalSum**2, 0


    
    
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


from functools import partial
if __name__ == '__main__':

    repeat = 100_000_0
    num_processes = 16  # Number of processes (usually number of cores on your CPU)
    
    # First compute averages
    avrX = parallel_execution(repeat, num_processes, lotteryAvrX)
    avrS = parallel_execution(repeat, num_processes, lotteryAvrS)

    # Create pickable function objects with the averages "baked in"
    dispersion_x_with_avg = partial(lotteryDispersionX, avrX)
    dispersion_s_with_avg = partial(lotteryDispersionS, avrS)

    # Pass these to parallel_execution
    disX = parallel_execution(repeat, num_processes, dispersion_x_with_avg)
    disS = parallel_execution(repeat, num_processes, dispersion_s_with_avg)

    avrXsqt = parallel_execution(repeat, num_processes, lotteryAvrXSquere)
    avrSsqt = parallel_execution(repeat, num_processes, lotteryAvrSSquere)
    
    
    disXmath = avrXsqt - avrX ** 2
    disSmath = avrSsqt - avrS ** 2
    
    avrXS = parallel_execution(repeat, num_processes, lotteryAvrXS)
    
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
    # os.system('cls' if os.name == 'nt' else 'clear')
    
    
    qxy = (avrXS - avrS * avrX) / math.sqrt(disX * disS)
    
    # # print all the results
    print(f"Average of X: {avrX}")
    print(f"Average of S: {avrS}")
    # print(f"Average of both: {avr12}")
    print(f"Dispersion of X: {disX}")
    print(f"Dispersion of S: {disS}")
    
    print(f"Dispersion of X (math): {disXmath}")
    print(f"Dispersion of S (math): {disSmath}")
    print(f"Correlation coefficient: {qxy}")
    