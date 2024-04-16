import sys
input = sys.stdin.readline
SCORE_LIST = []
for _ in range(int(input())):
    DICE_LIST = sorted(map(int, input().split()))
    if DICE_LIST[0] == DICE_LIST[3]:
        SCORE_LIST.append(50000 + DICE_LIST[0] * 5000)
    elif DICE_LIST[0] == DICE_LIST[2] or DICE_LIST[1] == DICE_LIST[3]:
        SCORE_LIST.append(10000 + DICE_LIST[1] * 1000)
    elif DICE_LIST[0] == DICE_LIST[1] and DICE_LIST[2] == DICE_LIST[3]:
        SCORE_LIST.append(2000 + DICE_LIST[0] * 500 + DICE_LIST[2] * 500)
    elif DICE_LIST[0] == DICE_LIST[1]:
        SCORE_LIST.append(1000 + DICE_LIST[0] * 100)
    elif DICE_LIST[2] == DICE_LIST[3] or DICE_LIST[1] == DICE_LIST[2]:
        SCORE_LIST.append(1000 + DICE_LIST[2] * 100)
    else:
        SCORE_LIST.append(DICE_LIST[3] * 100)
print(max(SCORE_LIST))
