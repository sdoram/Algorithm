T = int(input())
answer = list(map(int, input().split()))
SCORE = 0
TOTAL_SCORE = 0
for a in answer:
    if a:
        SCORE += 1
    else:
        SCORE = 0
    TOTAL_SCORE += SCORE
print(TOTAL_SCORE)