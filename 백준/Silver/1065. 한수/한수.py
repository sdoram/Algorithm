N = int(input())

count = min(N, 99)
for i in range(100, N+1):
    X = list(map(int, str(i)))
    if X[2]-X[1] == X[1]-X[0]:
        count += 1
        
print(count)