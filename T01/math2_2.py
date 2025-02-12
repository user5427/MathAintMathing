from My_Probability.combinations import A_Cycle, Checker
from My_Probability.multiplier import A_Cycler
from My_Probability.static_calculation import A

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

    if homesCalled[(list[calls - 1]-1) // phones] == 2:
        return True
    else:
        return False


a_Cycle = A_Cycler(totalPhones, calls)
total = A(totalPhones, calls)
found = Checker(a_Cycle, demaskedAtLastCall, True)
print(found)
print(found/total)