import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    seat = [[m+n*M for m in range(1, M+1)] for n in range(N)]
    try:
        print(seat[11][3])
    except IndexError:
        print(-1)