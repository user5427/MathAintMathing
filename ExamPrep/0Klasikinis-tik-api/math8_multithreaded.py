

import math
from random import random
from multiprocessing import Pool

from tqdm import tqdm

cards = 52
bugnai = 13
takes = 5

listWhereTheClubIs = [1,2]  # positions where the club can be (0-indexed)

cardsList = []
for i in range(cards):
    if i < bugnai:
        cardsList.append(1)  # 1 represents a club
    else:
        cardsList.append(0)  # 0 represents a non-club


def cards():
    cardsCopy = cardsList.copy()
    
    taken = []
    for _ in range(takes):
        card = int(random() * len(cardsCopy))  # pick a random card
        taken.append(cardsCopy[card])  # add the card to the taken list
        cardsCopy.pop(card)  # remove the card from the deck        
        
    # Check if the second or third card is a club
    # use list listWhereTheClubIs
    for club_position in listWhereTheClubIs:
        if club_position < len(taken) and taken[club_position] == 0:
            continue
        elif club_position < len(taken) and taken[club_position] == 1:
            return (1, 0)
    
    return (0, 0)    
    
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
    
    avr1 = parrallel_execution(repeat, num_processes, cards)
    
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # print all the results
    print(f"Average: {avr1}")