import sys
n, m, M, T, R = map(int, sys.stdin.readline().split())
MINUTE = 0
PRESENT_PULSE = m
if m+T > M: # 운동을 1분만 해도 최대 맥박을 초과하는 경우
    print(-1)
else:
    while n != 0:
        if PRESENT_PULSE+T <= M: # 운동을 해도 괜찮은 경우
            PRESENT_PULSE += T # 맥박 증가
            n -= 1 # 운동시간 감소
        else: # 휴식
            PRESENT_PULSE = PRESENT_PULSE - R if PRESENT_PULSE - R > m else m # 맥박 감소 or 초기 맥박 고정
        MINUTE += 1
    print(MINUTE)