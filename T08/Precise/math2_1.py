import math


n = 42
a = 39
b = 28
x = 255.4


totalM = a + b
toSurpass = b * n + x

mGreater = toSurpass / totalM
mCeil = math.ceil(mGreater)

n = n + 1 # 0 to n

prob = 1 / n

gudStuff = 0
for i in range(mCeil, n):
    gudStuff += prob
    
print(1 - gudStuff)
# gud