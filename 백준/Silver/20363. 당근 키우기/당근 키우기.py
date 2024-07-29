X, Y = map(int, input().split())
print(max(X, Y) + min(X, Y) + int(min(X, Y)*0.1))