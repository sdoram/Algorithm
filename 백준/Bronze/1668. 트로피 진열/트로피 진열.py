import sys
TROPHY_LIST = []
COUNT = 1
REVERSE_COUNT = 1
for _ in range(int(sys.stdin.readline())):
    TROPHY_LIST.append(int(sys.stdin.readline()))
CURRENT_TROPHY = TROPHY_LIST[0]
for i in TROPHY_LIST:
    if CURRENT_TROPHY < i:
        CURRENT_TROPHY = i
        COUNT += 1
REVERSE_CURRENT_TROPHY = TROPHY_LIST[-1]
for i in TROPHY_LIST[::-1]:
    if REVERSE_CURRENT_TROPHY < i:
        REVERSE_CURRENT_TROPHY = i
        REVERSE_COUNT += 1
print(COUNT, REVERSE_COUNT, sep='\n')