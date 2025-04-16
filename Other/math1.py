
digits = []

for i in range(10):
    digits.append(0)

for i in range(1, 1001):
    for digit in str(i):
        digits[int(digit)] += 1

for i in range(10):
    print(f"{i}: {digits[i]}")