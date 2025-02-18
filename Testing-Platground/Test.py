from My_Probability.deprecated_combinations import C_Cycle, Repeatable_Cycle


# list[i] == list[i+1]
def condition(list):
    for i in range(0, len(list)-1):
        if list[i] == list[i+1] + 1 or list[i] == list[i+1] - 1:
            return True
    return False

print(Repeatable_Cycle(5, 3, condition, True))
print(C_Cycle(5, 3, condition, True))



