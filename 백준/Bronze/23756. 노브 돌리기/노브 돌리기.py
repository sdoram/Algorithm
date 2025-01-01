N = int(input())
A = int(input())
total_angle = 0
for _ in range(N):
    B = int(input())
    total_angle += min(max(A, B) - min(A, B), min(A, B) + 360 - max(A, B))
    A = B
print(total_angle)