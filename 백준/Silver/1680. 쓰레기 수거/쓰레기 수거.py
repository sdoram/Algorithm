# 쓰레기 차가 돌아가는 경우
# 1. 쓰레기 용량이 도달했을 때
# 2. 그 지점의 쓰레기를 실었을 때 용량을 넘는 경우
# 3. 더 이상 쓰레기를 실을 지점이 없는 경우
import sys

input = sys.stdin.readline

def garbage_collection():
    # W = 쓰레기차의 용량, N = 지점의 개수
    W, N = map(int, input().split())
    # 현재 쓰레기차 용량, 합산거리, 편도거리
    current_capacity = 0
    total_distance = 0
    one_way = 0
    for i in range(N):
        # 거리, 쓰레기의 양
        x, w = map(int, input().split())
        # 도착한 곳의 쓰레기를 실어도 용량이 남은 경우
        if current_capacity + w < W:
            current_capacity += w
            total_distance += x - one_way
            if i == N-1:
                total_distance += x
        # 도착한 곳의 쓰레기를 실어서 용량이 꽉찬 경우
        elif current_capacity + w == W:
            current_capacity = 0
            total_distance += x*2 + x - one_way
            if i == N-1:
                total_distance -= x
        # 도착한 곳의 쓰레기를 실으면 용량이 넘치는 경우
        elif current_capacity + w > W:
            current_capacity = w
            total_distance += x*2 + x - one_way
            if i == N-1:
                total_distance += x
        one_way += x - one_way
    return total_distance

for _ in range(int(input())):
    print(garbage_collection())
