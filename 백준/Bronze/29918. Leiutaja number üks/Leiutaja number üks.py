A, B = map(int, input().split())
invention_list = []
for _ in range(5):
    N, M = map(int, input().split())
    invention_list.append(N + M*10)

print(max(max(invention_list) - (A + B*10) + 1, 0))