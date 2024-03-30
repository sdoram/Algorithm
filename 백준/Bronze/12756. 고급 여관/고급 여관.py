import sys
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
while True:
    A[1] -= B[0]
    B[1] -= A[0]
    if A[1] < 0:
        A[1] = 0
    if B[1] < 0:
        B[1] = 0
    if A[1] == 0 or B[1] == 0:
        break
if A[1] == 0 and B[1] == 0:
    print('DRAW')
else:
    print('PLAYER B' if A[1] == 0 else 'PLAYER A')