# 6. Urnoje yra keturi balti ir trys juodi rutuliai. Jie traukiami iš urnos vienas po kito, kol urna
# ištuštėja. Kokia tikimybė, kad pirmas ir paskutinis rutulys bus balti?

from math import comb  # Import the comb function for combinatorial calculations

black = 3
white = 4
total = black + white

totalPos = comb(total, white)
totalWhite = comb(total-2, white-2)

prob = totalWhite / totalPos
print("Probability that the first and last ball drawn are white: ", prob)