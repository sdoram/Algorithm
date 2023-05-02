import sys
M = int(sys.stdin.readline())
cups = [1, 2, 3]
for _ in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    X_location = cups.index(X)
    Y_location = cups.index(Y)
    cups[X_location], cups[Y_location] = cups[Y_location], cups[X_location]
print(cups[0])