import sys
A, B, C = map(int,sys.stdin.readline().split())
if A+B == C:
    print(f'{A}+{B}={C}')
elif A-B == C:
    print(f'{A}-{B}={C}')
elif A*B == C:
    print(f'{A}*{B}={C}')
elif A//B == C:
    print(f'{A}/{B}={C}')
# elif A == B + C:
#     print(f'{A}={B}+{C}')
elif A == B - C:
    print(f'{A}={B}-{C}')
# elif A == B * C:
#     print(f'{A}={B}*{C}')
elif A == B // C:
    print(f'{A}={B}/{C}')