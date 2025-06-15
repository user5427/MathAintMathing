from math import factorial

# 8. Kortu kaladėje yra 52 kortos, 13 iš ju – būgnai. Viena po kitos traukiamos penkios kortos.
# Kokia tikimybė, kad antroji arba trečioji korta (arba abi jos) bus būgnu?


total_cards = 52
total_clubs = 13
takes = 5


def arrangements(n, k):
    return factorial(n) // factorial(n - k)

total = arrangements(total_cards, takes)

good1 = total_clubs * (total_cards - total_clubs) * (total_cards - total_clubs - 1) * (total_cards - 3) * (total_cards - 4)  # 
good2 = (total_cards - total_clubs) * (total_cards - total_clubs - 1) * (total_cards - total_clubs - 2) * (total_cards - 3) * (total_cards - 4)  #

prob1 = good1 / total  # Probability that the second card is a club
prob2 = good2 / total  # Probability that the third card is a club

totalprob                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   = 1 - prob1 - prob2

print(totalprob)