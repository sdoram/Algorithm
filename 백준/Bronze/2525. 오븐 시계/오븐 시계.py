H, M = map(int, input().split())
cooking_time = int(input())
M += cooking_time
while M > 59:
    M -= 60
    H += 1
if H > 23:
    H -= 24
print(H, M)
