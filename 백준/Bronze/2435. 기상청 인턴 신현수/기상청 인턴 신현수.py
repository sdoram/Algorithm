N, K = map(int, input().split())
temperature = list(map(int, input().split()))
print(max([sum(temperature[i:K+i]) for i in range(N - K + 1)]))