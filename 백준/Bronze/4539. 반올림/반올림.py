for _ in range(int(input())):
    x = list(map(int, list(input())))[::-1]
    for i in range(len(x)-1):
        if x[i] >= 5:
            x[i+1] += 1
        x[i] = 0
    print(''.join(map(str, x[::-1])))
