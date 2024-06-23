X, Y = map(int, input().split())
print(*[3 if i % Y == 0 and i % X == 0 else 1 if i % Y == 0 else 2
        for i in range(1, X*Y+1) if i % X == 0 or i % Y == 0], sep='')