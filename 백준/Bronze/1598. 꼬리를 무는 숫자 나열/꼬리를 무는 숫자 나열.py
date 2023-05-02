N, M = map(int, input().split())
if N > M:
    N, M = M, N
width = (M-1)//4 - (N-1)//4
length = abs(width*4+N - M)
print(width+length)