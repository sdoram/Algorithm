n = int(input())
A = input()
B = input()
print(sum([1 for i in range(n) if A[i] != B[i]]))