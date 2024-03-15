import sys
AVERAGE = 0
for _ in range(5):
    SCORE = int(sys.stdin.readline())
    AVERAGE += SCORE if SCORE > 40 else 40
print(AVERAGE//5)