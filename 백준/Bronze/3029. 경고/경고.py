import sys
input = sys.stdin.readline
CURRENT_TIME = list(map(int, sys.stdin.readline().split(':')))
SCHEDULE_TIME = list(map(int, sys.stdin.readline().split(':')))
CURRENT_TIME_SECONDS = CURRENT_TIME[0] * 3600 + CURRENT_TIME[1] * 60 + CURRENT_TIME[2]
SCHEDULE_TIME_SECONDS = SCHEDULE_TIME[0] * 3600 + SCHEDULE_TIME[1] * 60 + SCHEDULE_TIME[2]
if CURRENT_TIME_SECONDS >= SCHEDULE_TIME_SECONDS:
    SCHEDULE_TIME_SECONDS += 86400 - CURRENT_TIME_SECONDS
else:
    SCHEDULE_TIME_SECONDS -= CURRENT_TIME_SECONDS
H, M, S = str(SCHEDULE_TIME_SECONDS // 3600), str(SCHEDULE_TIME_SECONDS % 3600 // 60), str(SCHEDULE_TIME_SECONDS % 3600 % 60)
print(H.zfill(2), M.zfill(2), S.zfill(2), sep=':')