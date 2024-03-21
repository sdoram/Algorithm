import sys
for _ in range(int(sys.stdin.readline())):
    A, B, X = map(int,sys.stdin.readline().split())
    print(A*(X -1) + B)