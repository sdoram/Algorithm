N,M,K = map(int, input().split())
X = [input().split('1') for _ in range(N)]
print(sum([sum([Z.count('0')-K+1 for Z in Y if Z.count('0'*K) > 0]) for Y in X]))