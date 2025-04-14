N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(sum([A[i] - B[i] for i in range(N) if A[i] > B[i]]))