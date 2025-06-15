# 2. Bandymas: triju žaidėju žaidimas kamuoliu. Vienas iš ju ima kamuoli, perduoda kitam, tas
# dar kitam. Kam perduoti kamuoli, žaidėjas pasirenka atsitiktinai, pasirinkimo tikimybės vieno-
# dos. Kokia tikimybė, kad pradėjęs žaidimą gaus kamuoli tik po 4 perdavimu?

ppl = 3  # number of players
throws = 4  # number of passes
total = (ppl - 1) ** throws
good = (ppl - 1) * (ppl - 2) ** (throws - 2) * ppl  # valid paths where the player receives the ball only after 4 passes

probability = good / total
print("Probability that the player receives the ball after 4 passes (intermediate passes possible): ", probability)

throws = throws
total2 = ppl * (ppl - 1) ** throws
good2 = ppl * (ppl - 1) * (ppl - 2) ** (throws - 1)
probability2 = good2 / total2
print("Probability that the player receives the ball only after 4 passes : ", probability2)