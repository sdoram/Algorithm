N = int(input())
T = map(int, input().split())
total = (N - 1) * 8 + sum(T)
print(total // 24, total % 24)
