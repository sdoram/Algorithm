import sys, bisect

input = sys.stdin.readline

N, M = map(int, input().split())
sort_list = sorted([int(input()) for _ in range(N)])

for _ in range(M):
    Q = int(input())
    # 이진 탐색으로 Q가 들어갈 수 있는 sort_list의 위치 찾기
    idx = bisect.bisect_left(sort_list, Q)
    # len(sort_list) > idx는 idx가 max(sort_list)보다 크면 len(sort_list)+1이므로 sort_list[idx] == Q에서 발생하는 에러 방지용
    # sort_list[idx] == Q는 찾아낸 들어갈 수 있는 위치의 숫자와 비교해서 같은지 판단
    print(idx if len(sort_list) > idx and sort_list[idx] == Q else -1)