import sys

input = sys.stdin.readline

N, M = map(int, input().split())
consumer = sorted([int(input()) for _ in range(M)], reverse=True)
expected_profit = {}

for i, c in enumerate(consumer, start=1):
    expected_profit[c] = c * min(i, N, M)
    
print(*sorted([[key, value] for key, value in expected_profit.items()], key=lambda x:(x[1], -x[0]), reverse=True)[0])