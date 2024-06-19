import sys

input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break
    case = [input().split() for _ in range(N)]
    tallest_height = max([c[1] for c in case])
    name = [c[0] for c in case if c[1] == tallest_height]
    print(*name)