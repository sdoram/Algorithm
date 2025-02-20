n, d = map(int, input().split())
t = [int(input()) for _ in range(n)]
for i in t:
    print(d // sum(t) * i)