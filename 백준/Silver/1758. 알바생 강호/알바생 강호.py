N = sorted([int(input()) for _ in range(int(input()))], reverse=True)
print(sum([max(n-i, 0) for i, n in enumerate(N)]))