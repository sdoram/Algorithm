N, M = map(int, input().split())
A = list(map(int, input().split()))[::-1]
sum_A = 0
if sum(A) < M:
    print(-1)
else:
    for i, a in enumerate(A):
        sum_A += a
        if sum_A >= M:
            print(len(A) - i)
            break