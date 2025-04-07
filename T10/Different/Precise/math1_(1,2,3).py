import math
from My_Probability.count_calculators import C


m0 = 6
m1 = 6
m2 = 4

val0 = 0
val1 = 1
val2 = 2

buying = 3

SMax = buying * val2
XMax = buying


grid = []

for needed2 in range(XMax+1):
    grid.append([])
    for j in range(SMax+1):
        if j // val2 >= needed2:
            sum = val2 * needed2
            needed1 = j - sum
            needed0 = buying - needed2 - needed1
            if needed1 > m1:
                grid[needed2].append(0)
                continue
            if needed0 > m0 or needed0 < 0:
                grid[needed2].append(0)
                continue
            
            prob = C(m0, needed0) * C(m1, needed1) * C(m2, needed2)
            prob /= C(m0 + m1 + m2, buying)
            grid[needed2].append(prob)
        else:
            grid[needed2].append(0)
        
        
# print(grid)
for i in range(len(grid)):
    string = ""
    for j in range(len(grid[i])):
        string += f"{grid[i][j]:8.4f} |"

    print(string)            
    print("-" * len(string))


# summ all the probabilities
sum = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        sum += grid[i][j]
        
# sum all of the rows seperately
row_sum = []
for i in range(len(grid)):
    row_sum.append(0)
    for j in range(len(grid[i])):
        row_sum[i] += grid[i][j]
        
Ex = 0
for i in range(len(row_sum)):
    Ex += row_sum[i]*i
    
Dx = 0
for i in range(len(row_sum)):
    Dx += row_sum[i] * (i - Ex)**2
    
print(f"Ex: {Ex}")
print(f"Dx: {Dx}")

# sum of all the columns separately
col_sum = []
for i in range(len(grid[0])):
    col_sum.append(0)
    for j in range(len(grid)):
        col_sum[i] += grid[j][i]
        
Es = 0
for i in range(len(col_sum)):
    Es += col_sum[i]*i
    
Ds = 0
for i in range(len(col_sum)):
    Ds += col_sum[i] * (i - Es)**2
    
print(f"Es: {Es}")
print(f"Ds: {Ds}")

# now find E[XS]
Exs = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        Exs += grid[i][j] * i * j   
        
qXS = (Exs - Ex * Es) / math.sqrt(Dx * Ds)
print(f"qXS: {qXS}")     
        
