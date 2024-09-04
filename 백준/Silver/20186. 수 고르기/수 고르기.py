N, K = map(int, input().split())
print(sum(sorted(list(map(int, input().split())), reverse=True)[:K]) - sum([k for k in range(K)]))