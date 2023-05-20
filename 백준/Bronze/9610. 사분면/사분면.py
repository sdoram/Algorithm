from sys import stdin

Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
AXIS = 0
for _ in range(int(stdin.readline())):
    x, y = map(int, stdin.readline().split())
    if 0 in [x, y]:
        AXIS += 1
    elif x > 0 and y > 0:
        Q1 += 1
    elif x < 0 and y > 0:
        Q2 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    elif x > 0 and y < 0:
        Q4 += 1
print(f"Q1: {Q1}\nQ2: {Q2}\nQ3: {Q3}\nQ4: {Q4}\nAXIS: {AXIS}")
