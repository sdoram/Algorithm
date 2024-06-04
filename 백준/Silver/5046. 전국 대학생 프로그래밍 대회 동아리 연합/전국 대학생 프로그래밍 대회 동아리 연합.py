import sys 

input = sys.stdin.readline

def holding_a_meeting():
    # 참가자, 예산, 호텔 수, 선택 가능 주
    N, B, H, W = map(int, input().split())

    cost = B + 1

    for _ in range(H):
        price = int(input())
        max_people = max(map(int, input().split()))
        # 예산 >= 가격 * 사람 수  and 최대 수용 >= 참가자 
        if B >= price * N and max_people >= N:
            cost = min(cost, price * N)
            
    return cost if cost < B else 'stay home'

print(holding_a_meeting())