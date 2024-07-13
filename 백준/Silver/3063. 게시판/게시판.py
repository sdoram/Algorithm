for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    my_post = (x2-x1) * (y2-y1)
    other_post = max(0, min(x4, x2) - max(x3, x1)) * max(0, min(y4, y2) - max(y3, y1))
    print(my_post - other_post)
