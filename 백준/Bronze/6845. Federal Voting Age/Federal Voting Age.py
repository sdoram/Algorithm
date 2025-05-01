for _ in range(int(input())):
    y, m, d = map(int, input().split())
    if y == 1989:
        if m == 1 or m == 2 and d <= 27:
            print('Yes')
        else:
            print('No')
    elif y > 1989:
        print('No')
    else:
        print('Yes')