import math


n = 61
a = 21
b = 18
x = 226.48


totalM = a + b
toSurpass = b * n

mGreater = toSurpass / totalM
mCeil = math.ceil(mGreater)

n = n + 1 # 0 to n

prob = 1 / n

gudStuff = 0
for i in range(mCeil, n):
    gudStuff += prob
    
print(gudStuff)
# gud