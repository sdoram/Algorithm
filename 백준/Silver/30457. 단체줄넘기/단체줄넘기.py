A = [0]
B = [0]

N = int(input())
C = list(map(int, input().split()))

for c in sorted(C):
    if c > max(A):
        A.append(c)
    elif c > max(B):
        B.append(c)

print(len(A)-1 + len(B)-1)