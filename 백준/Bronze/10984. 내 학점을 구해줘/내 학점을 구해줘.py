for _ in range(int(input())):
    total, num = 0, 0
    for _ in range(int(input())):
        x, y = input().split()
        x, y = int(x), float(y)
        total += x * y
        num += x
    print(num, round(total / num, 1))