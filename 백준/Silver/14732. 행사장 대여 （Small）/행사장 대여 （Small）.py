area = [[False for _ in range(500)] for _ in range(500)]
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            area[x][y] = True

print(sum([sum(a) for a in area]))