
import math


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

counts = []
p = 50

for i in range(0, primes.__len__()):
    counts.append(math.floor(p / primes[i]) / 100)
    
print(counts)

average = 0
for i in range(0, primes.__len__()):
    average += counts[i] * primes[i]
print(average)

