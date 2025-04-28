a, b, c = 0, 0, 0
for _ in range(int(input())):
    d = list(map(int, input().split()))
    a += d[0]
    b += d[1]
    c += d[2]
    f = min(a, b, c)
    if f >= 30:
        print(f)
        a -= f
        b -= f
        c -= f
    else:
        print('NO')