import sys

input = sys.stdin.readline

score_list = []

for _ in range(int(input())):
    N = list(map(int, input().split()))
    score_list.append(max(N[:2]) + sum(sorted(N[2:], reverse=True)[:2]))
print(max(score_list))