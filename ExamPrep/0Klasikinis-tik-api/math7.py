# 7. Kortu kaladėje yra 52 kortos. Atsitiktinai traukiamos penkios kortos. Kokia tikimybė, kad
# tarp ištrauktuju kortu bus lygiai du tūzai?


total = 52
tuzai = 4
takes = 5
from math import comb  # Import the comb function for combinatorial calculations


totalCombs = comb(total, takes)  # Total combinations of drawing 5 cards from 52
goodCombs = comb(tuzai, 2) * comb(total - tuzai, takes - 2)  # Combinations where exactly 2 cards are aces
probability = goodCombs / totalCombs  # Probability of drawing exactly 2 aces in 5 cards
print("Total combinations of drawing 5 cards from 52: ", totalCombs)
print("Combinations where exactly 2 cards are aces: ", goodCombs)
print("Probability of drawing exactly 2 aces in 5 cards: ", probability)