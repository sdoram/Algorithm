N = int(input())
A = input()
B = input()
print(N - max(len([1 for i in range(N) if A[i] == B[i]]), 0))