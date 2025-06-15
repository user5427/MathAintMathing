# 1. Vienetiniame kvadrate nubrėžta viena istrižainė.  ̨ Kokia tikimybė, kad atsitiktinai šiame
# kvadrate parinkto taško atstumas iki istrižainės  ̨ bus didesnis už 0,5? Paaiškinkite brėžiniu.

import math


length = 1  # Length of the square's side
other = 0.5

total_area = length ** 2  # Total area of the square

c = math.sqrt(2 * (other ** 2))  # Distance from the center to the diagonal
d = length - c

area = 2 * (d ** 2 / 2)

print("Total area of the square: ", total_area)
print("Area where the distance to the diagonal is greater than 0.5: ", area)