N, K = map(int, input().split())
print(max([int(str(N*k)[::-1]) for k in range(1, K+1)]))