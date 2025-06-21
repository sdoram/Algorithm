X, L, R = map(int, input().split())
print(X if L <= X <= R else R if R - X <= X - L else L)