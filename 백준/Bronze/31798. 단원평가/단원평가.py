A, B, C = map(int, input().split())
if C == 0:
    print(int((A+B)**0.5))
else:
    print(C**2 - (A+B))