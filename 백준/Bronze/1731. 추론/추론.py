N = [int(input()) for _ in range(int(input()))]
print(N[-1] + N[1] - N[0] if N[1] - N[0] == N[2] - N[1] else N[-1] * N[1] // N[0])