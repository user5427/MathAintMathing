# 5. Bandymas: trys draugai laiko egzaminą. Kadangi jie atsiskaitė už pratybu užduotis, tai
# garantuotai išlaikys egzaminą, t.y., gaus vieną iš ivertinimu  5,6,7,8,9,10. Kokia ivykio  „lygiai du
# draugai gaus vienodus pažymius“ tikimybė?

totalFriends = 3
gradesList = [5, 6, 7, 8, 9, 10]  # possible grades
totalCombinations = len(gradesList) ** totalFriends  # total combinations of grades
goodCombinations = len(gradesList) * 1 * (len(gradesList) - 1) * totalFriends

probability = goodCombinations / totalCombinations  # probability of exactly two friends having the same grade
print("Total combinations of grades for 3 friends: ", totalCombinations)
print("Combinations where exactly two friends have the same grade: ", goodCombinations) 
prob = goodCombinations / totalCombinations
print("Probability that exactly two friends will have the same grade: ", prob)