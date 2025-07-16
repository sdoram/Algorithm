A, B, C = map(int, input().split())
print(sum([str(i).count(str(C)) for i in range(A, B+1)]))