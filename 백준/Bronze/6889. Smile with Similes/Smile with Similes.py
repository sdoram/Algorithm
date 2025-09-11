n = int(input())
m = int(input())
X = [input() for _ in range(n)]
Y = [input() for _ in range(m)]
for x in X:
    for y in Y:
        print(f'{x} as {y}')