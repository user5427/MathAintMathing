import math

# Parametrai
N = 12  # uždavinių skaičius
n = 6   # studentų skaičius

# Funkcija, skaičiuojanti tikimybę, kad bent trys studentai gaus tą patį uždavinį
def calculate_probability(N, n):
    # Bendras galimų pasirinkimų skaičius
    total_outcomes = N ** n

    # Skaičiuojame palankius įvykius, kai bent trys studentai turi tą patį uždavinį
    favorable_outcomes = 0

    # Naudojame kombinacijas, kad suskaičiuotume galimus pasiskirstymus
    for k in range(3, n + 1):  # k yra studentų, turinčių tą patį uždavinį, skaičius
        # Pasirenkame, kuris uždavinys bus pasikartojantis
        for u in range(1, N + 1):
            # Pasirenkame, kurie studentai gaus šį uždavinį
            ways_to_choose_students = math.comb(n, k)
            # Likę studentai turi gauti skirtingus uždavinius
            remaining_students = n - k
            ways_to_assign_remaining = math.perm(N - 1, remaining_students)
            # Palankių įvykių skaičius
            favorable_outcomes += ways_to_choose_students * ways_to_assign_remaining

    # Tikimybė
    probability = favorable_outcomes / total_outcomes
    return probability

# Apskaičiuojame tikimybę
probability = calculate_probability(N, n)
print(f"Tikimybė, kad bent trys studentai gaus tą patį uždavinį: {probability:.4f}")