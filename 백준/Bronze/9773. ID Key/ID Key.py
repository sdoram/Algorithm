for _ in  range(int(input())):
    p = input()
    A = str(int(p[10:]) * 10 + sum(map(int, list(p))))
    print(int(A) + 1000 if int(A) < 1000 else A[-4:] if len(A) <= 5 else A)