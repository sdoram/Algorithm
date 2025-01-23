N, I = map(int, input().split())
print(sorted([input() for _ in range(N)])[I-1])