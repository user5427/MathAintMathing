import math

from My_Probability.cyclers import Repeatable_Cycler
from My_Probability.evaluators import Evaluator


# its all wrong whatever the hell this is

m = 9
n = 6
k1 = 3
k2 = 4

prob1 = m / (n + m)
prob2 = n / (n + m)

def throwCoin(length):
    listOfProbs = []
    
    listOfCoins = []
    for i in range(length): 
        listOfCoins.append(1)
    
    while True:
        oneCount = listOfCoins.count(1)
        twoCount = listOfCoins.count(2)
        
        prob = (prob1**oneCount) * (prob2**twoCount) * math.comb(length, oneCount)   
        sumt = oneCount + twoCount * 2
        listOfProbs.append((prob, sumt))
        
        #change two ones to one two if possible, otherwise break
        if oneCount > 0:
            listOfCoins.remove(1)
            listOfCoins.append(2)
        else:
            break
            
    return listOfProbs


avr1 = 0
avr2 = 0

for i in throwCoin(k1):
    avr1 += i[0] * i[1]
    
for i in throwCoin(k2):
    avr2 += i[0] * i[1]
    
print(avr1)
print(avr2)


avr1sqrt = 0
avr2sqrt = 0

for i in throwCoin(k1):
    avr1sqrt += i[0] * i[1] ** 2
    
for i in throwCoin(k2):
    avr2sqrt += i[0] * i[1] ** 2
    
print(avr1sqrt)
print(avr2sqrt)

mathDispersion1 = avr1sqrt - avr1**2
mathDispersion2 = avr2sqrt - avr2**2

print(mathDispersion1)
print(mathDispersion2)


mult = k1 * avr1 - avr1sqrt / k1

# for i in throwCoin(k1):
#     for j in throwCoin(k2):
#         mult += i[0] * j[0] * i[1] * j[1]

# print(mult)
    


qxy = (mult - avr1 * avr2) / math.sqrt(mathDispersion1 * mathDispersion2)

print(qxy)

