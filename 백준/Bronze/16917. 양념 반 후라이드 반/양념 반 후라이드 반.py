import sys
input = sys.stdin.readline
A, B, C, X, Y = map(int, sys.stdin.readline().split())

if  A + B < C*2:
    print(A*X + B*Y)
elif X > Y:
    print(min(A*(X-Y) + (Y*2*C), X*2*C))
else:
    print(min(B*(Y-X) + (X*2*C), Y*2*C))