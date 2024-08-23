import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = set(input().rstrip() for _ in range(N))
print(sum([1 if input().rstrip() in S else 0 for _ in range(M)]))