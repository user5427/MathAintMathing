p = 0.65
m = 3
n = 4

kSum = 0
for k in range(0, n):
    kSum += p * (1 - p)**(k)
    
    
kGud = 0
for k in range(0, m):
    kGud += p * (1 - p)**(k)
    
res = kGud / kSum
print(res)