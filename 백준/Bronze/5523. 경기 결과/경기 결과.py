import sys

input = sys.stdin.readline

A_SCORE = 0
B_SCORE = 0
for _ in range(int(input())):
    A, B = map(int, input().split())
    if A > B:
        A_SCORE += 1
    elif B > A:
        B_SCORE += 1
        
print(A_SCORE, B_SCORE)