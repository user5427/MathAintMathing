from random import random


white = 28
black = 100 - white
k = 2

whiteProb = white / (white + black)
blackProb = black / (white + black)

def taking():
    whitCount = 0
    
    # repeat experiment until whiteCount is k
    
    turnNr = 0
    while whitCount < k:
        if random() < whiteProb:
            whitCount += 1
            
        if whitCount == k:
            if turnNr == 0:
                return 1
            else:
                return 0
            
        
        turnNr += 1
        if turnNr > 2:
            turnNr = 0
            
            
repeat = 10000000
count = 0
for i in range(0, repeat):
    if taking() == 1:
        count += 1
        
print(count / repeat)