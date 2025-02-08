N = int(input())
for i in range(1, N+1):
    menu = list(input().split())
    if i == N:
        for m in menu:
            print(m)