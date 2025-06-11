# 4. Bandymas: trys draugai laiko egzaminą. Kadangi jie atsiskaitė už pratybu užduotis, tai
# garantuotai išlaikys egzaminą, t.y., gaus vieną iš ivertinimu  5,6,7,8,9,10. Kiek palankiu baigčiu
# turi ivykis:  „ne visi draugai bus ivertinti  skirtingai“?



numOfFriends = 3
grades = [5, 6, 7, 8, 9, 10]  # possible grades

allDifferent = len(grades) * (len(grades) - 1) * (len(grades) - 2)  # all different grades
totalCombinations = len(grades) ** numOfFriends  # total combinations of grades

notAllDifferent = totalCombinations - allDifferent  # combinations where not all grades are different

print("Total combinations of grades for 3 friends: ", totalCombinations)
print("Combinations where not all friends have different grades: ", notAllDifferent)