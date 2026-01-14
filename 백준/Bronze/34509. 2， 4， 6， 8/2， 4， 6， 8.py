for i in range(10, 100):
    x = str(i)
    if '8' not in x:
        if sum([int(y) for y in x]) % 6 == 0:
            if int(x[::-1]) % 4 == 0:
                print(x)