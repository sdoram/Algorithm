for _ in range(3):
    yut = list(map(int, input().split()))
    if sum(yut) == 4:
        print("E")
    if sum(yut) == 3:
        print("A")
    if sum(yut) == 2:
        print("B")
    if sum(yut) == 1:
        print("C")
    if sum(yut) == 0:
        print("D")