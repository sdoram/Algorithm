while True:
    A, B = map(int, input().split())
    if sum([A,B]) == 0:
        break
    if A - B == 1:
        print(0, 0)
    elif (A-B) % 2 == 0:
        print((A-B) // 2, 0)
    else:
        print((A-B-3) // 2, 1)