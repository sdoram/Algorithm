N, Q = map(int, input().split())
line = [1 for _ in range(N)]

def balloon(L, I):
    for i in range(L-1, N, I):
        line[i] = 0
      
for _ in range(Q):
    L, I = map(int, input().split())
    balloon(L, I)
    
print(sum(line))