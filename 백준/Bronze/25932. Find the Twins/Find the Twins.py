n = int(input())
for i in range(n):
    mack, zack = False, False
    x = list(input().split())
    if '18' in x:
        mack = True
    if '17' in x:
        zack = True
    print(' '.join(x))
    print('both' if mack and zack else 'mack' if mack else 'zack' if zack else 'none')
    if i != n-1:
        print()