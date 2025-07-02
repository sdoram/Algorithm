import sys

input = sys.stdin.readline

D = int(input())

while True:
    N = int(input())
    if D > N:
        D += N
    else:
        break
print(D)