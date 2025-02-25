from My_Probability.deprecated_combinations import A_Cycle, Checker
from My_Probability.cyclers import A_Cycler
from My_Probability.count_calculators import A

houses = 8
phones = 4
calls = 4

totalPhones = houses * phones
demaskedAtExact = 0

def demaskedAtLastCall(list):
    homesCalled = []
    for j in range(0, houses):
        homesCalled.append(0)
    for j in range(0, calls):
        homesCalled[(list[j]-1) // phones] += 1

    notDem = False
    avoid = (list[calls-1]-1) // phones
    for j in range(0, houses):
        if homesCalled[j] >= 2 and j != avoid:
            notDem = True
            break

    if homesCalled[(list[calls - 1]-1) // phones] == 2 and not notDem:
        # print(list)
        return True
    else:
        return False


a_Cycle = A_Cycler(totalPhones, calls)
total = A(totalPhones, calls)
found = Checker(a_Cycle, demaskedAtLastCall, False)
print(found)
print(found/total)