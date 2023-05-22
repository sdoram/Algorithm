for _ in range(int(input())):
    x, y = map(int, input().split())
    z = divmod(x, y)
    print(f"You get {z[0]} piece(s) and your dad gets {z[1]} piece(s).")
