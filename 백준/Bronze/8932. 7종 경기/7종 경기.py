import sys
input = sys.stdin.readline
CONSTANT_LIST = [[9.23076,26.7,1.835,0],  # 트랙은 0, 필드는 1
                 [1.84523, 75, 1.348, 1],
                 [56.0211, 1.5, 1.05, 1],
                 [4.99087, 42.5, 1.81, 0],
                 [0.188807, 210, 1.41, 1],
                 [15.9803, 3.8, 1.04, 1],
                 [0.11193, 254, 1.88, 0],
                 ]
for _ in range(int(input())):
    RECORD = map(int, input().split())
    TOTAL_SCORE = 0
    for O, R in enumerate(RECORD):
        if CONSTANT_LIST[O][3] == 0: # 트랙 경기일 경우
            TOTAL_SCORE += int(CONSTANT_LIST[O][0] * (CONSTANT_LIST[O][1] - R) ** CONSTANT_LIST[O][2])
        else: # 필드 경기일 경우
            TOTAL_SCORE += int(CONSTANT_LIST[O][0] * (R - CONSTANT_LIST[O][1]) ** CONSTANT_LIST[O][2])
    print(TOTAL_SCORE)