A, B, C = map(int, input().split())
D = int(input())
C += D
if C >= 60:
    B += C//60
    C -= C//60 * 60
if B >= 60:
    A += B//60
    B -= B//60 * 60
if A >= 24:
    A -= A//24 * 24

print(A, B, C)