n = int(input())
for i in range(1, n+1):
    print(i, end=' ')
    if i != n:
        if i % 6 == 0:
            print('Go!', end=' ')
    else:
        print('Go!')