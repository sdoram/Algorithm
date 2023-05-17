A, K = map(int, input().split())
A = list(map(int, input().split(",")))
for _ in range(K):
    instance_A = []
    for a in range(1, len(A)):
        instance_A.append(A[a] - A[a - 1])
    A = instance_A
print(*A, sep=",")