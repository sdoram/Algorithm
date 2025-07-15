total = 0

for _ in range(int(input())):
    ki = input()
    total += ki.count('A') * 4
    total += ki.count('K') * 3
    total += ki.count('Q') * 2
    total += ki.count('J') * 1
print(total)