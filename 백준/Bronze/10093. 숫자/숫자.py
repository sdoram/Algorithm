A, B = map(int, input().split())
print(max(max(A, B)-min(A, B)-1, 0))
if max(A, B)-min(A, B)-1 > 0:
    print(' '.join([str(i) for i in range(min(A, B)+1, max(A, B))]))