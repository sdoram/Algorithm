for _ in range(int(input())):
    x, y = map(float, input().split())
    print(round(max(x,y) - min(x,y), 1))