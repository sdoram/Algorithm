import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
CAR_COUNT = [m]
for _ in range(n):
    x, y = map(int, input().split())
    m += x - y
    CAR_COUNT.append(m)
print(max(CAR_COUNT) if min(CAR_COUNT) >= 0 else 0)