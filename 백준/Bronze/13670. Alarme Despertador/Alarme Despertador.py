while True:
    H1, M1, H2, M2 = map(int, input().split())
    if sum([H1, M1, H2, M2]) == 0:
        break
    T1 = H1 * 60 + M1
    T2 = H2 * 60 + M2
    if T1 > T2:
        print(1440 + T2 - T1)
    else:
        print(T2 - T1)