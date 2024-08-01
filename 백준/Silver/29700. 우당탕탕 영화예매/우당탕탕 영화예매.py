N, M, K = map(int, input().split())

seat =  [input().split('1') for _ in range(N)]
print(sum([sum([s.count('0')-K+1 for s in S if s.count('0'*K) >= 1]) for S in seat]))