import sys
input = sys.stdin.readline
N, Q = map(int,input().split())
SCORE = [int(input()) for _ in range(N)]
for _ in range(Q):
    TQ = int(input())
    CURRENT_SCORE = 0
    for I, S in enumerate(SCORE):
        CURRENT_SCORE += S
        if CURRENT_SCORE-1 >= TQ:
            ANSWER = I+1
            break
    print(ANSWER)