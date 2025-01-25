cost = 0
for _ in range(int(input())):
    H, B, K = map(int, input().split())
    if B - H > 0:
        cost += (B - H) * K
print(cost)