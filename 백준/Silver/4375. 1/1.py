while True:
    try:
        n = int(input())
        i = 1
        while i % n != 0:
            i *= 10
            i += 1
        print(len(str(i)))
    except EOFError:
        break