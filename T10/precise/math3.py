import math

from My_Probability.cyclers import Repeatable_Cycler
from My_Probability.evaluators import Evaluator


m = 7
n = 9
k1 = 4
k2 = 6

prob1 = m / (n + m)
prob2 = n / (n + m)



# def throwCoin(k1):
#     listOfProbs = []
    
#     for i in range(k1, k1*2+1):
#         listOfCoins = []
#         # Calculate how many 1's and 2's we need to make sum i
#         one_count = min(m, i)  # Start with as many 1's as possible, up to m
#         remaining = i - one_count
#         # Check if we can't reach the sum exactly with 2's (odd remaining)
#         if remaining % 2 == 1 and one_count > 0:
#             one_count -= 1  # Remove one 1-coin
#             remaining = i - one_count  # Recalculate remaining
#         two_count = min(n, remaining // 2)  # Add 2's to reach sum i
        
#         # Add 1's to the list
#         for _ in range(one_count):
#             listOfCoins.append(1)
        
#         # Add 2's to the list
#         for _ in range(two_count):
#             listOfCoins.append(2)
            
#         print(listOfCoins)
#         print(i)
        
#         prob = 0
#         while True:
#             oneCount = listOfCoins.count(1)
#             twoCount = listOfCoins.count(2)
            
#             prob += (prob1**oneCount) * (prob2**twoCount) * math.comb(k1, oneCount)   
            
#             #change two ones to one two if possible, otherwise break
#             if oneCount > 1:
#                 listOfCoins.remove(1)
#                 listOfCoins.remove(1)
#                 listOfCoins.append(2)
#             else:
#                 break
            
#         listOfProbs.append((prob, i))
        
            
#     return listOfProbs

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

# def throwCoinMMMMM(length):
#     minSum = length
#     maxSum = length * 4
#     listOfProbs = []
    
#     for i in range(minSum, maxSum + 1):
#         listOfProbs.append((0, i))

    
#     def checkfunc(list):
#         print(list)
#         oneCount = list.count(1)
#         twoCount = list.count(2)
#         twoCount += list.count(3)
#         fourCount = list.count(4)
        
#         prob = (prob1**oneCount) * (prob2**twoCount) * ((prob2 ** 2) ** fourCount)
#         sumt = oneCount + twoCount * 2 + fourCount * 4
#         listOfProbs.append((prob, sumt))
        
#     r_iterator = Repeatable_Cycler(4, length)
#     ev = Evaluator(r_iterator, checkfunc)
#     ev.Evaluate()
            
#     return listOfProbs


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


mult = 0

for i in throwCoin(k1):
    for j in throwCoin(k2):
        mult += i[0] * j[0] * i[1] * j[1]

print(mult)
    


qxy = (mult - avr1 * avr2) / math.sqrt(mathDispersion1 * mathDispersion2)

print(qxy)




# print(prob1)
# print(prob2)


# avr1 = k1 * (1 * prob1 + 2 * prob2)
# avr2 = k2 * (1 * prob1 + 2 * prob2)

# print(avr1)
# print(avr2)

# avr1sqrt = k1 * (1 * prob1 + 4 * prob2)
# avr2sqrt = k2 * (1 * prob1 + 4 * prob2)


# print(avr1sqrt)
# print(avr2sqrt)

# dispersion1 = avr1sqrt - avr1**2
# dispersion2 = avr2sqrt - avr2**2

# print(dispersion1)
# print(dispersion2)


# disp1 = k1 * ((1 - avr1) ** 2 * prob1 + (2 - avr2)**2 * prob2)
# disp2 = k2 * ((1 - avr1) ** 2 * prob1 + (2 - avr2)**2 * prob2)
# print(disp1)
# print(disp2)
