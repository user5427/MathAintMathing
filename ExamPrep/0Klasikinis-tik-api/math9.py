# 9. Voke – 8 skirtingos nuotraukos, tik viena ju spalvota. Vieną po kitos traukiate 5 nuotraukas
# ir rikiuojate i  eilę. Kokia tikimybė, kad antroji eilės nuotrauka bus spalvota?

import math


pictures = 8
takes = 5

prob = (7 / 8) * (1 / 7)

print(f'Tikimybė, kad antroji eilės nuotrauka bus spalvota: {prob:.3f}')

# C(1,1) * C(1, 1) * C(6, 3) / C(8, 5)

# good = 6*5*4*3
# total = 7*6*5*4*3

# print(f'Gera kombinacija: {good}, visos kombinacijos: {total}')
# print(f'Tikimybė, kad antroji eilės nuotrauka bus spalvota: {good / total:.3f}')


# Key insight: Due to the symmetry of random sampling without replacement, each position (1st, 2nd, 3rd, 4th, 5th) has an equal probability of containing the colored photo.
# Method 1 - Symmetry argument:
# Since we're randomly arranging 5 photos out of 8, and there's only 1 colored photo, that colored photo is equally likely to appear in any of the 5 positions. Therefore:
# P(2nd photo is colored) = P(1st photo is colored) = P(3rd photo is colored) = ... = P(5th photo is colored)
# The probability that the colored photo appears somewhere in our sequence of 5 is:
# P(colored photo in sequence) = (Number of ways to choose 5 photos including the colored one) / (Total ways to choose 5 photos)
# = C(7,4) / C(8,5) = 35/56 = 5/8
# Since this probability is equally distributed among the 5 positions:
# P(2nd photo is colored) = (5/8) ÷ 5 = 1/8 = 0.125