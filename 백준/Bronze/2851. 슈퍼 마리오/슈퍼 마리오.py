import sys
SCORE_LIST = [int(sys.stdin.readline()) for _ in range(10)]
TOTAL_SCORE = SCORE_LIST[0]
for i in range(10):
    CURRENT_SCORE = sum([x for x in SCORE_LIST[:i+1:]])
    if abs(100 - TOTAL_SCORE) >= abs(100 - CURRENT_SCORE):
        TOTAL_SCORE = CURRENT_SCORE
print(TOTAL_SCORE)