def Cleopatra():
    N, X = map(int, input().split())
    limit_list = list(map(int, input().split()))
    while True:
        for i, l in enumerate(limit_list, start=1):
            if X > l:
                return i
            X += 1
print(Cleopatra())