while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(min(A*30+B*40, A*35+B*30, A*40+B*20))