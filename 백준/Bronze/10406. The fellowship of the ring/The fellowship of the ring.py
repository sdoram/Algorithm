W, N, P = map(int, input().split())
print(sum([1 for p in map(int, input().split()) if W <= p <= N]))