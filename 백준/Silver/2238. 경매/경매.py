import sys
input = sys.stdin.readline
U, N = map(int, sys.stdin.readline().split())

def auction_system(U, N):
    bid = []
    bid_range = dict()
    for _ in range(N):
        S, P = input().split()
        P = int(P)
        if P in bid_range: # 이미 있을 때
            bid_range[P] += [S]
        else:
            bid_range[P] = [S]
        bid.append([S, P])
    # 같은 가격을 제시한 사람의 숫자로 오름차순 정렬 후, 낮은 가격으로 다시 오름차순 정렬
    successful_bid = sorted(bid_range.items(), key=lambda x:(len(x[1]), x[0]))[0]
    return print(successful_bid[1][0], successful_bid[0])

auction_system(U, N)