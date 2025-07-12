N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(sum([3 if A[i] > B[i] else 1 if A[i] == B[i] else 0 for i in range(N)]))