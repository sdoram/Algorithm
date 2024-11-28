S, D, I, L, N = map(int, input().split())
print(max(int((N - (S + D + I + L) / 4) * 4), 0))