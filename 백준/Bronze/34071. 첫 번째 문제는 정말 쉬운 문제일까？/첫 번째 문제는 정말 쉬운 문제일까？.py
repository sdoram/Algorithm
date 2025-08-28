X = [int(input()) for _ in range(int(input()))]
print('hard' if X[0] == max(X) else 'ez' if X[0] == min(X) else '?')