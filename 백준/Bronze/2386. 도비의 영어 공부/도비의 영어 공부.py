while True:
    a = input().lower()
    if a[0] == "#":
        break
    print(a[0], a[1:].count(a[0]))