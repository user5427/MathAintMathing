
# 1. Bandymas: lošimo kauliuko ir dvieju ̨ monetos metimas. Kaip pavaizduotumėte vienodai
# galimas tokio bandymo baigtis? Kiek yra šio bandymo baigčiu ̨?


totalCombinations = 6 * 2 * 2
print("Total combinations for rolling a die and flipping two coins: ", totalCombinations)

waysToRepresent = [[die, coin1, coin2] for die in range(1, 7) for coin1 in ['H', 'T'] for coin2 in ['H', 'T']]
print("Ways to represent the outcomes:")
for outcome in waysToRepresent:
    print(outcome)