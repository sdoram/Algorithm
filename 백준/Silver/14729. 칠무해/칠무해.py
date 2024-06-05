# 소수점 셋째 자리까지 받기
# 10,000,000까지 입력 받을 수 있으므로 시간복잡도 고려하기

# 시간 복잡도가 문제인줄 알았으나 공간복잡도 때문에 메모리 초과 발생

import sys, heapq

input = sys.stdin.readline

def use_heapq(N):
    score_list = [-float(input()) for _ in range(7)]
    heapq.heapify(score_list)

    for _ in range(N-7):
        score = -float(input())
        if score > score_list[0]:
            heapq.heappushpop(score_list, score)
    score_list = sorted([-s for s in score_list])
    return [format(s, '.3f') for s in score_list]

print(*use_heapq(int(input())), sep='\n')