p = 51
q = 69
k = 6

p = p / 100
q = q / 100


prob = 0
avr = 0
duration = 100000
for i in range(0, duration):
    pos = 1 - (1 - p) * (1 - q)
    nop = (1 - pos) ** i
    
    prob += pos * nop
    avr += (i + 1) * pos * nop
    
print(1/(1 - (1 - p) * (1 - q)))
# print(avr)