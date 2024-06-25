N, M = map(int, input().split())

area = [list(input()) for _ in range(N)]
size = N*M

for i, column in enumerate(area):
    for j, c in enumerate(column):
        if j >= 1 and c == column[j-1] == '-':
            size -= 1
        elif i != N-1 and c == area[i+1][j] == '|':
            size -= 1
            
print(size)