input()
N = list(map(int, input().split()))
X = N[0]
count = 0
for n in N:
    if X < n:
        count += 1
    X = n
print(count)