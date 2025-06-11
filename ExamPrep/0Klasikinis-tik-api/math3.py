# 3. Studentas žino penkis būdus pasiteisinti dėl neatliktos užduoties. Jis neatliko triju užduočiu.
# Keliais būdais jis gali pasiteisinti, jeigu to paties pasiteisinimo iš eilės dvieju kartu naudoti negal-
# ima?

ways = 5  # number of excuses
exc = 3  # number of excuses used
total_excuses = ways ** exc  # total combinations of excuses
good_excuses = ways * (ways - 1) ** (exc - 1)  # valid combinations where the same excuse is not used consecutively
prob = good_excuses / total_excuses  # probability of valid combinations
print("Probability of valid excuses combinations (no consecutive same excuses): ", prob)
print("Total combinations of excuses: ", total_excuses)
print("Valid combinations of excuses (no consecutive same excuses): ", good_excuses)