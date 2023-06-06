X = [int(n) for n in input()]
COUNT = 0
while len(X) > 1:
    X = [int(n) for n in str(sum(X))]
    COUNT += 1
print(COUNT)
print("YES" if X[0] % 3 == 0 else "NO")