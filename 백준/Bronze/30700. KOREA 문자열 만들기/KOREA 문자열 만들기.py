import sys
S = sys.stdin.readline().rstrip()
KOREA = ['K', 'O', 'R', 'E', 'A']
COUNT = 0
while True:
    try:
        CURRENT_LOCATION = S.index(KOREA[COUNT%5])
        S = S[CURRENT_LOCATION:]
        COUNT += 1
    except ValueError:
        print(COUNT)
        break