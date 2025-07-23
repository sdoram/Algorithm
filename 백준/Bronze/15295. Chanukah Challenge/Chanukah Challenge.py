for _ in range(int(input())):
    x, y = map(int, input().split())
    print(x, sum([i for i in range(y+1)])+y)