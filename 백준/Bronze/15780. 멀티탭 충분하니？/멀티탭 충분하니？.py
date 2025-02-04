N, K = map(int, input().split())
A = list(map(int, input().split()))
print('YES' if N <= sum([(a+1) // 2 for a in A]) else 'NO')