A, B = map(int, input().split())
C = int(input())
T = (A * 60 + B + C) % 1440
print(T // 60, T % 60)