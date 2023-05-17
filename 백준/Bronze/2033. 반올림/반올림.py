N = int(input())
for i, n in enumerate(range(1, len(str(N))), 1):
    if N % 10**i // 10 ** (i - 1) >= 5:
        N += 10**i - (N % 10**i)
    else:
        N -= N % 10**i
print(N)
