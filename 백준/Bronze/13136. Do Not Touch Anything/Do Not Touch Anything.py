R, C, N = map(int, input().split())
A = R // N + 1 if R / N > R // N else R // N
B = C // N + 1 if C / N > C // N else C // N
print(A * B)